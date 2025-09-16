# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Database](#database)
    - [CAP Theorem (Brewer's theorem)](#cap-theorem-brewers-theorem)
    - [Trade-offs (CA, CP, AP)](#trade-offs-ca-cp-ap)
    - [ACID](#acid)
    - [BASE](#base)
    - [ACID Vs. BASE](#acid-vs-base)
    - [Choosing a Database](#choosing-a-database)
    - [Isolation Levels](#isolation-levels)
    - [Primary Indexing Vs. Secondary Indexing](#primary-indexing-vs-secondary-indexing)
    - [Optimistic Locking Vs. Pessimistic Locking](#optimistic-locking-vs-pessimistic-locking)
    - [Assume there is no database locking, how deploy this lock mechanism in application level](#assume-there-is-no-database-locking-how-deploy-this-lock-mechanism-in-application-level)
    - [Redis Vs. RabbitMQ Vs. Kafka](#redis-vs-rabbitmq-vs-kafka)
    - [Is RabbitMQ a database?](#is-rabbitmq-a-database)
    - [How to prevent multiple workers consume the same event in RabbitMQ](#how-to-prevent-multiple-workers-consume-the-same-event-in-rabbitmq)
    - [What are different type of exchanges in RabbitMQ](#what-are-different-type-of-exchanges-in-rabbitmq)
    - [How to handle failed or lost published events](#how-to-handle-failed-or-lost-published-events)
    - [How Redis handles concurrency and race-condition when being used as distributed locking mechanism?](#how-redis-handles-concurrency-and-race-condition-when-being-used-as-distributed-locking-mechanism)

## Database

### CAP Theorem (Brewer's theorem)

In a distributed database/system, you cannot simultaneously guarantee all three of these properties:

- **Consistency (C)**

  - Every read gets the most recent write (all nodes see the same data at the same time).
  - Example: If I write X=10, any read immediately after should return 10.

- **Availability (A)**

  - Every request receives a response, even if it might not be the latest version of the data.
  - System stays responsive even under failure.

- **Partition Tolerance (P)**

  - The system continues to function despite network partitions (nodes not being able to communicate).

CAP theorem says:
In the presence of a **network partition**, you must choose between **Consistency** and **Availability**.

---

### Trade-offs (CA, CP, AP)

- **CP (Consistency + Partition tolerance)**

  - Sacrifice availability during network failures.
  - Strongly consistent systems. (e.g. Banking Systems)
  - Example: HBase, MongoDB (with strong consistency configs).

- **AP (Availability + Partition tolerance)**

  - Sacrifice strict consistency → eventual consistency is allowed.
  - Prioritize always responding, even if data might be stale. (e.g. Social Media Feeds)
  - Example: Cassandra, DynamoDB.

- **CA (Consistency + Availability)**

  - Theoretically possible only if no network partitions exist → not practical in distributed systems.
  - Example: traditional single-node RDBMS (like PostgreSQL on one machine).

---

### ACID

`ACID` is a set of properties that guarantee reliable transactions in databases (especially relational ones like PostgreSQL, MySQL, Oracle).

1. **Atomicity**

   - "All or nothing."
   - A transaction is indivisible: either all operations succeed, or none do.
   - Example: In a money transfer:
     - Deduct $100 from Alice
     - Add $100 to Bob
     - If adding fails, the deduction is rolled back.

2. **Consistency**

   - Transactions bring the database from one valid state to another valid state, following all rules, constraints, and triggers.
   - Example: If a column must be unique, inserting a duplicate violates consistency → transaction fails.

3. **Isolation**

   - Concurrent transactions should not interfere with each other.
   - Intermediate states are not visible to other transactions.
   - Different isolation levels exist:
     - Read Uncommitted (dirty reads allowed)
     - Read Committed
     - Repeatable Read
     - Serializable (highest, behaves like transactions are sequential).

4. **Durability**

   - Once a transaction is committed, it is permanent, even if the system crashes right after.
   - Achieved via **write-ahead logs (WALs)**, **replication**, and **persistent storage**.

---

### BASE

Many NoSQL databases (Cassandra, DynamoDB, CouchDB, etc.) follow the BASE model to favor scalability and availability in distributed systems.

1. **Basically Available**

- The system guarantees availability, but not necessarily consistency at all times.
- Even under failure, it tries to respond — possibly with stale data.
- Example: Amazon DynamoDB or Cassandra nodes may return older values instead of failing.

2. **Soft State**

- The system state may change over time, even without input.
- Because of replication and eventual consistency, different nodes may temporarily hold different values.
- Example: A write to one replica may not immediately be visible on another.

3. **Eventual Consistency**

- Given enough time (assuming no new updates), all replicas will converge to the same state.
- Strong consistency is sacrificed for performance and fault tolerance.
- Example: In Cassandra, a read might not show the latest write, but eventually all nodes sync up.

---

### ACID Vs. BASE

| Property     | **ACID**                                                    | **BASE**                                                                    |
| ------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| Consistency  | Strong consistency                                          | Eventual consistency                                                        |
| Availability | Can sacrifice availability (during conflicts or partitions) | Prioritizes availability                                                    |
| Use Case     | Banking, reservations, systems needing strong guarantees    | Large-scale distributed systems, social media, e-commerce with huge traffic |

---

### Choosing a Database

1. **Data Model & Structure**

- If data is highly relational with complex joins, foreign keys, and transactions → a Relational DB (PostgreSQL, MySQL, Oracle) makes sense.
- If data is document-oriented, hierarchical, or schema-flexible (e.g., product catalogs, JSON-like structures) → a Document Store (MongoDB, Couchbase) is better.
- If workload is time-series (metrics, IoT, monitoring) → use a Time-Series DB (InfluxDB, TimescaleDB).
- If workload is graph-like (social networks, recommendation engines) → a Graph DB (Neo4j, ArangoDB) fits best.

2. **Consistency vs Availability (CAP theorem)**

- If the system needs strict correctness (e.g., financial transactions) → choose a strongly consistent ACID DB (PostgreSQL, MySQL, Oracle).
- If the system prioritizes high availability and scale (e.g., social feeds, analytics) → a BASE / eventually consistent DB (Cassandra, DynamoDB) is more suitable.

3. **Scalability Requirements**

- For a single-region, moderate traffic system → vertical scaling with a relational DB works well.
- For globally distributed, high-traffic apps → need a horizontally scalable DB like Cassandra, DynamoDB, or CockroachDB.

4. **Query Patterns & Access Needs (Read/Write Heavy)**

- Do we need ad-hoc queries, aggregations, joins? → SQL databases shine.
- Do we mostly fetch by key/value lookups? → Key-Value stores (Redis, DynamoDB).
- Do we need real-time analytics? → Columnar DBs (ClickHouse, BigQuery).

5. **Transaction Requirements**

- Strong transactional integrity (ACID) → SQL DBs (Postgres, MySQL).
- Eventual consistency is okay (shopping cart, likes, logs) → NoSQL (MongoDB, Cassandra).

6. **Ecosystem, Tooling & Operational Overhead**

- Does the team have experience with SQL or NoSQL?
- Is there cloud-native support (AWS RDS, DynamoDB, GCP Spanner)?
- Do we need easy migrations, backups, replication?

- **Example**

  - Banking system / Payment gateway → PostgreSQL (ACID, strong consistency).
  - Social media feed → Cassandra / DynamoDB (BASE, high availability).
  - Product catalog with flexible schema → MongoDB.
  - Analytics dashboard → ClickHouse or BigQuery.
  - Cache / Session store → Redis.

---

### Isolation Levels

Concurrency Anomalies to Know:

- **Dirty Read** – A transaction reads uncommitted data from another transaction.
- **Non-Repeatable Read** – A transaction reads the same row twice and gets different results (because another transaction updated it in between).
- **Phantom Read** – A transaction re-runs a query (e.g., SELECT ... WHERE condition) and new rows appear/disappear (because another transaction inserted/deleted rows).

- **Read Uncommitted (Lowest level)**

  - ✅ Allows dirty reads.
  - Transactions can see uncommitted changes from others.
  - Rarely used in practice (can lead to inconsistent states).
  - Example use: analytics queries where stale data is acceptable.

- **Read Committed**

  - 🚫 Prevents dirty reads.
  - Each read sees only committed data.
  - But still allows non-repeatable reads and phantoms.
  - This is the default in PostgreSQL & Oracle.

- **Repeatable Read**

  - 🚫 Prevents dirty reads and non-repeatable reads.
  - Guarantees that if you read a row twice in the same transaction, it won’t change.
  - Still allows phantom reads (new rows might appear that match the query condition).
  - This is the default in MySQL (InnoDB).

- **Serializable (Highest level)**

  - 🚫 Prevents all three anomalies (dirty, non-repeatable, phantom).
  - Transactions are executed as if they were serial (one after another).
  - Strongest guarantee but lowest concurrency (can cause locking/contention).
  - Best for financial apps requiring correctness over performance.

| Isolation Level  | Dirty Read | Non-Repeatable Read | Phantom Read |
| ---------------- | ---------- | ------------------- | ------------ |
| Read Uncommitted | ✅ Allowed | ✅ Allowed          | ✅ Allowed   |
| Read Committed   | ❌ No      | ✅ Allowed          | ✅ Allowed   |
| Repeatable Read  | ❌ No      | ❌ No               | ✅ Allowed   |
| Serializable     | ❌ No      | ❌ No               | ❌ No        |

---

### Primary Indexing Vs. Secondary Indexing

- **Primary Index**

  - Built on the primary key (or clustering key) of a table.
  - The data file itself is ordered by this key (clustered index).
  - Each table can have only one primary index.
  - Lookup is very fast because the index order matches the physical storage order.

- **Secondary Index**

  - Built on non-primary key attributes (non-clustering key).
  - The data file is not ordered by this key.
  - A table can have multiple secondary indexes.
  - Provides fast lookups on attributes other than the primary key.
  - Usually implemented with an extra pointer (row ID / primary key reference) that links back to the actual row.Think of it as an extra search table that helps find rows quickly without scanning everything.
  - too many secondary indexes slow down writes (since every insert/update must update all relevant indexes).

| Feature             | Primary Index                         | Secondary Index                        |
| ------------------- | ------------------------------------- | -------------------------------------- |
| **Key Type**        | Built on primary key / clustering key | Built on non-primary key columns       |
| **Ordering**        | Data stored in order of index         | Data not stored in index order         |
| **Count per Table** | Only one                              | Many allowed                           |
| **Access Method**   | Direct, since data is aligned         | Needs extra lookup (to row/primary)    |
| **Performance**     | Faster for key-based searches         | Slight overhead (extra pointer lookup) |

---

### Optimistic Locking Vs. Pessimistic Locking

- **Pessimistic Locking**
  - Idea: “Assume conflicts will happen, so block others until I’m done.”
  - A transaction acquires **a lock on the row (or table) before reading or updating it**.
  - Other transactions that try to access the same data must **wait until the lock is released**.
  - Pros:
    - Prevents **conflicts** and **race conditions** reliably.
    - Safer for highly contended data.
  - Cons:
    - Reduced concurrency → other transactions may block a long time.
    - Can lead to deadlocks if not managed carefully.

```sql
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- Now row id=1 is locked until COMMIT/ROLLBACK
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

- **Optimistic Locking**

  - Idea: “Conflicts are rare, so let everyone work, and check for conflicts at commit.”
  - **Doesn’t block others while reading**.
  - Each row has a **version number (or timestamp)**.
  - When updating, the transaction checks if the version is still the same:
    - If yes → update succeeds.
    - If no → someone else changed it → `transaction fails` → `retry` needed.
  - Pros:
    - Higher **concurrency**, since no blocking.
    - Good when conflicts are rare.
  - Cons:
    - Extra retries if conflicts are frequent.
    - More application logic required.

```sql
-- Suppose accounts has a "version" column
SELECT id, balance, version FROM accounts WHERE id = 1;

-- Later, update only if version hasn’t changed
UPDATE accounts
SET balance = balance - 100, version = version + 1
WHERE id = 1 AND version = 5;

-- If no rows updated → conflict detected → retry needed
```

---

### Assume there is no database locking, how deploy this lock mechanism in application level

1. In-Memory Lock (Single Instance App)

If your app runs on one server (no multiple processes/instances):
Use a `sync.Mutex` or `sync.RWMutex` in Go.

Ensures only one goroutine at a time accesses the critical section.

```go
var mu sync.Mutex
var balance int = 100

func withdraw(amount int) {
    mu.Lock()
    defer mu.Unlock()
    balance -= amount
}
```

2. Distributed Locks (Multi-Instance / Cluster)

- If you have multiple app instances (microservices, replicas, etc.), you need a shared lock mechanism.

- **Redis-based Locking (Redlock)**:
  - Use Redis `SETNX` (set if not exists) + `expiration`.
  - Libraries implement this (`redsync` for Go).

```go
// Pseudo-logic
if redis.SETNX("lock:account:1", "user-uuid", expiry) {
    // got lock, do work
    // ...
    redis.DEL("lock:account:1")
} else {
    // lock already held
}
```

- **Database Advisory Locks**
  - PostgreSQL supports `advisory locks` at the app level:
    - Lock is tied to your connection, not a row.
    - Use arbitrary numbers/keys (like a user ID).

```sql
-- Acquire a lock
SELECT pg_advisory_lock(12345);

-- Release lock
SELECT pg_advisory_unlock(12345);
```

- **ZooKeeper / etcd Locks**

  - Useful in distributed systems.
  - Provide consensus-based locks.
  - Heavier but reliable for large-scale apps.

---

### Redis Vs. RabbitMQ Vs. Kafka

| Feature                            | **Redis** (Pub/Sub / Streams)                                           | **RabbitMQ** (AMQP Broker)                                           | **Kafka** (Event Streaming)                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Type**                           | In-memory datastore with pub/sub and streams                            | Traditional message broker                                           | Distributed event streaming/log platform                                                      |
| **Persistence**                    | Optional (RDB / AOF); Pub/Sub is ephemeral                              | Durable queues on disk                                               | Always persistent (commit log)                                                                |
| **Throughput**                     | Very high (microseconds latency)                                        | Medium–high (100k+ msgs/sec)                                         | Extremely high (millions msgs/sec)                                                            |
| **Scalability**                    | Limited (Redis Cluster, sharding)                                       | Clustering, but scaling is harder                                    | Native horizontal scalability                                                                 |
| **Ordering**                       | Not guaranteed in Pub/Sub; Streams maintain sequence within a stream    | Guaranteed per queue                                                 | Guaranteed per partition                                                                      |
| **Delivery Promise**               | **At-most-once** (Pub/Sub) <br> **At-least-once** (Streams if ACK used) | **At-most-once**, **At-least-once**, **Exactly-once** (with plugins) | **At-least-once** by default; **Exactly-once** supported with transactions (since Kafka 0.11) |
| **Repeatable (Re-read messages?)** | ❌ Pub/Sub: No replay <br> ✅ Streams: Replay possible while retained   | ❌ Once a consumer ACKs, message is gone                             | ✅ Yes, consumers can replay from offsets (log retained for hours–days–forever)               |
| **Routing Flexibility**            | Basic (channels/streams)                                                | Rich (direct, fanout, topic, headers exchanges)                      | Partition-based, less flexible than RabbitMQ                                                  |
| **Use Case Fit**                   | Lightweight messaging, caching, leaderboards, chat apps                 | Background job processing, workflows, task distribution              | Event-driven systems, analytics pipelines, log aggregation, event sourcing                    |

---

### Is RabbitMQ a database?

NO, It’s a **message broker** (a type of middleware) that helps different services and applications communicate by passing messages between them.

What RabbitMQ does:

- Implements **AMQP** (Advanced Message Queuing Protocol).
- Stores messages _temporarily_ in queues until a consumer receives them.
- Ensures reliable delivery (at-least-once or exactly-once depending on setup).
- Supports publish/subscribe, work queues, routing, priority queues, etc.
- Used for decoupling services, asynchronous processing, and scaling workloads.

### How to prevent multiple workers consume the same event in RabbitMQ

1. Use a single queue per consumer group

- If you want only one worker out of many to consume, put them on the same queue. RabbitMQ will distribute load.
- Don’t bind multiple queues unless you want duplication.
- `Exchange → Queue (single) → Consumers (many)`

2. Enable manual acknowledgments

- Use `ack` after successful processing.
- This prevents RabbitMQ from redelivering unacked messages if your consumer is slow or crashes.

3. Idempotent consumers

- Since RabbitMQ only gives **at-least-once** delivery, you must make consumers _idempotent_ (safe to process the same message twice).
- E.g., track processed message IDs in DB/Redis.

4. Publisher confirms

- Ensure producers don’t re-publish the same message due to connection retries.
- Use publisher confirms (`confirm_select`) to avoid duplicates at the publishing side.

5. Avoid multiple brokers with uncoordinated queues

- If you have multiple RabbitMQ clusters/brokers without federation/shovel, each may get a copy of the message.
- Use a single RabbitMQ cluster or federation for consistent delivery.

### What are different type of exchanges in RabbitMQ

1. **Direct exchange** – routes messages by exact routing key.

- Example: routing key "`order.created`" → goes only to queues bound with that key.

2. **Fanout exchange** – broadcasts message to **all** bound queues, ignoring routing key.

- Example: sending notifications to all services.

3. **Topic exchange** – routes messages using patterns (`\*, #`).

- Example: `order.\*` → matches order.created, order.shipped.

### How to handle failed or lost published events

**Publisher Confirms / Acknowledgments**

- In RabbitMQ, enable publisher confirms.
- The **broker sends an ack** when it has safely stored the message.
- If you don’t get an ack (e.g., timeout), you retry.
- Guarantees the broker got the message, not just your client.

**Transactional Publishing**

Wrap **publishing in a transaction** (`RabbitMQ` and `Kafka` support this).
Either all messages succeed or none are published.
Slower, but good for critical cases (e.g., financial transactions).

**Retry with Backoff**

- On failure, retry sending the event after a delay.
- Use **exponential backoff + jitter** to avoid overwhelming the broker.
- Example: Retry after `2s → 4s → 8s → 16s …`.

**Dead Letter Queues (DLQ)**

- If a message fails to publish/consume after several attempts, send it to a DLQ.
- Later, investigate/reprocess it manually or with a recovery service.

**Idempotent Consumers**

- Even if the publisher retries and a message is delivered twice, consumers should handle duplicates gracefully.
- Add an event ID (UUID) and store processed IDs in a DB or cache (e.g., Redis SET).
- This is also effective when trying to achieve **exactly once** delivery promise.

**Outbox Pattern**

- Store the event in your **local database** inside the same transaction as your business logic.
- A background worker then reads from the “outbox table” and publishes to the broker.
- Guarantees no lost events if the publisher crashes.
- Very common with `Postgres + RabbitMQ/Kafka` setups.

**Monitoring & Alerts**

- Set up metrics for **dropped messages, unacked messages, DLQ size**.
- Alerts help you detect when events go missing.

---

### How Redis handles concurrency and race-condition when being used as distributed locking mechanism?

1. **Atomic Lock Acquisition**

- Use `SET key value NX PX <ttl>`:
  - `NX` → only set if not exists.
  - `PX <ttl>` → expiration (auto-release after timeout).
- This ensures only one client acquires the lock at a time.

```sh
SET lock:resource client-uuid NX PX 10000
```

→ If successful, client has lock for 10 seconds.

2. **Unique Identifier**

- The value stored in the lock (like client-uuid) identifies the owner.
- When releasing, client checks:

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("DEL", KEYS[1])
else
    return 0
end
```

Prevents a client from accidentally unlocking a lock it doesn’t own.

3. **Expiration (Avoiding Deadlocks)**

TTL ensures that if a client crashes or never releases, the lock eventually expires.
This **prevents permanent deadlock**.

4. **Redlock Algorithm (Distributed Safety)**

- For true distributed systems (multiple Redis nodes):
  - Acquire the lock on majority (`N/2 + 1`) of Redis nodes.
  - Only consider _lock acquired if you succeed on majority_.
  - Locks have the same TTL across nodes.
  - This reduces the chance that a single-node failure causes multiple clients to think they hold the lock.

---
