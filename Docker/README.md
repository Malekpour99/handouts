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
