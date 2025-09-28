# Docker

## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [ELK](#elk)
    - [Create Separate Network](#create-separate-network)
    - [Create Elasticsearch](#create-elasticsearch)
    - [Create Kibana](#create-kibana)
    - [Create Logstash](#create-logstash)
  - [ELK in Docker Compose](#elk-in-docker-compose)
    - [Defining `kibana_system` user password in `elasticsearch` service](#defining-kibana_system-user-password-in-elasticsearch-service)

## ELK

Setting up an ELK stack using only docker CLI and containers

### Create Separate Network

```sh
docker network create --driver bridge elk-net
```

### Create Elasticsearch

```sh
docker run -d --name elasticsearch --net elk-net -p 9200:9200 -p 9300:9300 -it -e bootstrap.memory_lock=true -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" -m 1GB -e discovery.type=single-node -v es_data_1:/usr/share/elasticesearch/data elasticsearch:8.18.0
```

- `-m 1GB`: Limits the container to a maximum of _1GB_ of memory at the Docker level.

- Environments
  - `bootstrap.memory_lock=true`: Tells Elasticsearch to try to lock memory to prevent swapping. This improves performance and is recommended in production.
  - Sets JVM options:
    - `Xms512m`: Initial heap size
    - `Xmx512m`: Maximum heap size
    - Ensures Elasticsearch starts with and never exceeds _512MB_ of heap memory.
  - `discovery.type=single-node`: Instructs Elasticsearch to run in single-node mode (i.e., no need to discover or wait for other nodes to form a cluster). Required for standalone or dev environments.

**Generating enrollment token and password**

```sh
docker exec -it elasticsearch sh

cd /usr/share/elasticsearch/bin

elasticsearch-reset-password -u elastic
# Generates a new password for 'elastic' (default super-user) and prints it in the terminal

elasticsearch-create-enrollment-token -s kibana
# Generates an enrollment token for 'kibana' service (-s = --scope)
```

### Create Kibana

```sh
docker run -d --name kibana --net elk-net -p 5601:5601 kibana:8:18.0

docker logs kibana (-f)
# check kibana logs for access-link and verification-code
```

1. Submit your enrollment code
2. Submit the verification code acquired from logs (if required)
3. Use 'elastic' username and its generated password to login

### Create Logstash

```sh
docker run -d --name logstash --net elk-net -v ./config:/etc/logstash/conf.d -p 5010:5000 logstash:8.18.0 logstash -f /etc/logstash/conf.d/logstash.conf
# Provided command after logstash image will override its default entrypoint!
```

## ELK in Docker Compose

When running ELK stack using docker compose, kibana requires a specific user (**kibana_system**) other than the default super-user of '_elastic_'!

```sh
docker compose exec -it elasticsearch sh

cd bin

elasticsearch-reset-password -u kibana_system
# Generates a new password for 'kibana_system' user and prints it in the terminal

elasticsearch-create-enrollment-token -s kibana
# Generates an enrollment token for 'kibana' service (-s = --scope)
```

### Defining `kibana_system` user password in `elasticsearch` service

1. Directly defining the password in the elasticsearch service and restarting all of the services afterwards:

```sh
docker exec -it elasticsearch bin/elasticsearch-reset-password -u kibana_system
```

- `elasticsearch` -> is the name of docker compose elasticsearch service container!

after confirmation, you will be prompted with the new password for `kibana_system` user, like this:

```text
Password for the [kibana_system] user successfully reset.
New value: <new-password>
```

Copy your new password and update these fields in your files:

- `kibana/kibana.yml` -> update `elasticsearch.password`
- `.env` -> update `KIBANA_PASSWORD`

Now everything is ready, restart your services!

```sh
docker compose restart
```

2. Using a setup complementary container alongside other ELK stack containers

```yaml
setup:
  image: elasticsearch:8.18.0
  container_name: elk_setup
  command: >
    bash -c '
      echo "Waiting for Elasticsearch availability";
      until curl -s http://elasticsearch:9200 | grep -q "missing authentication credentials"; do sleep 30; done;
      echo "Setting kibana_system password";
      until curl -s -X POST -u "elastic:${ELASTICSEARCH_PASSWORD}" -H "Content-Type: application/json" http://elasticsearch:9200/_security/user/kibana_system/_password -d "{\"password\":\"${KIBANA_PASSWORD}\"}" | grep -q "^{}"; do sleep 10; done;
      echo "Password setup complete!";
    '
  depends_on:
    elasticsearch:
      condition: service_healthy
  restart: "no"
  networks:
    - logging
```

- This service, uses elasticsearch APIs for setting the new password for `kibana_system` user!
