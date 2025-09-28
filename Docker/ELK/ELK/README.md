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

- make sure to name your environment file `.env` its the default file for reading environment variables; otherwise you must configure your docker compose file to read environments from another custom environment file!
- Make sure to define **strong and complex** passwords for `elastic` & `kibana_system` users and update their passwords in these files:

  - `.env` -> update `ELASTICSEARCH_PASSWORD` (for `elastic`)
  - `logstash/pipeline/logstash.conf` -> `output` - `elasticsearch`'s `password` (for `elastic`)
  - `logstash/config/logstash.yml` -> `xpack.monitoring.elasticsearch.password` (for `elastic`)
  - `.env` -> update `KIBANA_PASSWORD` (for `kibana_system`)
  - `kibana/kibana.yml` -> update `elasticsearch.password` (for `kibana_system`)

Start ELK docker compose in detached mode:

```sh
docker compose up -d
```

## Development Setup

Just run your services as usual:

```sh
docker compose up
```

- by adding `-d` flag, they will run in detached mode!

## Production Setup

If it's **INITIAL SETUP**:

1. Update these fields in your files:
   - `logstash/pipeline/logstash.conf` -> Comment/Remove `sincedb_path => "/dev/null"` from `input`'s `file` pipeline!
   - `logstash/pipeline/logstash.conf` -> update `environment` in `mutate` section to **`production`**!
2. Now, make sure to follow the **Initial Setup** process for the rest!

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
  - `Name`: `Django Logs`
  - `Index Pattern`: `django-logs*`
  - `Timestamp Field`: `@timestamp`
- Side Menu -> (Analytics) `Discover` -> select `django-logs` for Data View -> Refresh
  - Filter logs by `date`, `level`, `message`, etc.

## Further Improvements

Consider these as backlogs:

- Changing service port mappings
- Creating a certificate and Enabling SSL
- Defining new users with limited access instead of using default superusers (i.e. `elastic`)
