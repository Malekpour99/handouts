## Common Logstash Ports

| Port     | Purpose                       | Expose with `-p`?                                | Notes                            |
| -------- | ----------------------------- | ------------------------------------------------ | -------------------------------- |
| **5044** | Beats input (e.g. Filebeat)   | ✅ Yes, if sending Beats data from outside Docker | Most common input                |
| **5000** | TCP/UDP input (syslog or raw) | ✅ Yes, if used                                   | You can define it in your config |
| **9600** | Monitoring HTTP API           | 🔄 Optional                                      | Useful for health checks/metrics |
| **8080** | Custom HTTP input (if used)   | ✅ Only if configured                             | Not used by default              |

## Current Configuration Features

1. Listens on TCP port 5000 for JSON-formatted logs.
2. Adds a tag called test to each incoming log.
3. Sends the structured event to Elasticsearch for indexing