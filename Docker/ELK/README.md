## Understanding `ulimits` in Docker (Soft vs Hard Limits)

### 🔹 Soft Limit

- The **current limit** for a resource.
- Can be **modified by the process/user** (increased up to the hard limit).
- Meant to be flexible for normal operation.

### 🔹 Hard Limit

- The **maximum allowable limit** for a resource.
- Can **only be increased by a superuser (root)**.
- Acts as a **ceiling** for the soft limit.

### Elasticsearch benefits from locked memory to:

- Prevent swapping to disk.
- Improve performance and stability.

---

### Example

```yaml
ulimits:
  memlock:
    soft: 262144
    hard: 524288

    # The process starts with a soft limit of 262144.
    # It can raise the limit up to 524288 if needed and permitted.

ulimits:
  memlock:
    soft: -1
    hard: -1

    # -1 means no limit.
    # Allows Elasticsearch to lock as much memory as it needs.
    # Recommended with bootstrap.memory_lock=true for performance.
```

## Understanting `depends_on` in Docker Compose

`depends_on` option is used to express startup ordering between services and controls the order in which services are started, not their health or readiness.
By default it does not wait for services to be ready (i.e., accepting connections) — only that their containers have started.

If your services needs to wait for a service to be fully available, you'll need to implement some kind of wait-for-it logic, like:

- using _wait-for-it_ scripts or _conditions_
- adding retry logic in your services

### Docker Compose Conditions

| Condition                        | Description                                                                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_started`                | Waits until the dependent service **has been started** (i.e., the container is running), regardless of health. _(Default behavior if no condition is set)_ |
| `service_healthy`                | Waits until the dependent service **reports a healthy status** (requires a `healthcheck` in that service).                                                 |
| `service_completed_successfully` | Waits until the dependent service **exits with a `0` exit code** (typically used for one-shot or setup jobs).                                              |
