# ELK Stack Setup

## Table of Contents

- [ELK Stack Setup](#elk-stack-setup)
  - [Table of Contents](#table-of-contents)
  - [Initial Setup](#initial-setup)
  - [Development Setup](#development-setup)
  - [Production Setup](#production-setup)
  - [Kibana Dashboard](#kibana-dashboard)
    - [Defining a Data-View](#defining-a-data-view)
  - [Further Improvements](#further-improvements)

## Initial Setup

Navigate to ELK directory:

```sh
cd ELK
```

Create an environment file from the sample `.env.example`:

```sh
cp .env.example .env
```

make sure to name your environment file `.env` its the default file for reading environment variables; otherwise you must configure your docker compose file to read environments from another custom environment file!

Start ELK docker compose file for the first time:

```sh
docker compose up
```

after running your services, wait for them until you see this log from your `elasticsearch` service:

```json
{
  "@timestamp": "2025-09-27T16:53:38.313Z",
  "log.level": "INFO",
  "message": "Authentication of [kibana_system] was terminated by realm [reserved] - failed to authenticate user [kibana_system]",
  "ecs.version": "1.2.0",
  "service.name": "ES_ECS",
  "event.dataset": "elasticsearch.server",
  "process.thread.name": "elasticsearch[elasticsearch][generic][T#16]",
  "log.logger": "org.elasticsearch.xpack.security.authc.RealmsAuthenticator",
  "trace.id": "e2f0f4b36e7a27860d8cb0828bf86cc5",
  "elasticsearch.cluster.uuid": "IAVqvQo8RjOLOnRwy7w-uw",
  "elasticsearch.node.id": "cNVFwTtpRdSsRGK86S86Ug",
  "elasticsearch.node.name": "elasticsearch",
  "elasticsearch.cluster.name": "docker-cluster"
}
```

Now open a new terminal for setting-up `kibana_system` user, and enter below command:

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

Now everything is ready, restart your services:

```sh
docker compose restart
```

## Development Setup

Just run your services as usual:

```sh
docker compose up
```

- by adding `-d` flag, they will run in detached mode!

## Production Setup

If it's **INITIAL SETUP**:

1. Make sure to provide strong passwords for `elastic` user and update this password in these files:
   - `.env` -> update `ELASTICSEARCH_PASSWORD`
   - `logstash/pipeline/logstash.conf` -> `output` - `elasticsearch`'s `password`
   - `logstash/config/logstash.yml` -> `xpack.monitoring.elasticsearch.password`
2. Update these fields in your files:
   - `logstash/pipeline/logstash.conf` -> Comment/Remove `sincedb_path => "/dev/null"` from `input`'s `file` pipeline!
   - `logstash/pipeline/logstash.conf` -> update `environment` in `mutate` section to **`production`**!
3. Now, make sure to follow the **Initial Setup** process for the rest!

Now if everything is set, run your services in detached mode:

```sh
docker compose up -d
```

## Kibana Dashboard

After setting-up your services, Kibana dashboard is accessible through: `http://localhost:5601`
Use `elastic` user and its password for login.

### Defining a Data-View

- Side Menu -> (Management) `Stack Management` -> (Data) `Index Management` -> `Create Index` -> e.g. `django-logs`
- Side Menu -> (Management) `Stack Management` -> (Kibana) `Data Views` -> `Create Data View`:
  - `Name`: `django-logs`
  - `Index Pattern`: `django-logs*`
  - `Timestamp Field`: `@timestamp`
- Side Menu -> (Analytics) `Discover` -> select `django-logs` for Data View -> Refresh
  - Filter logs by `date`, `level`, `message`, etc.

## Further Improvements

Consider these as backlogs:

- Using strong and complex passwords for production
- Defining new users with limited access instead of using default superusers (i.e. `elastic`)
- Creating a certificate and Enabling SSL
- Changing service port mappings
- Exposing service ports instead of mapping them, when there is no need to access them from outside (i.e. `elasticsearch` & `logstash`)
