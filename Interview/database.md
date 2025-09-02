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
    - [Redis Vs. RabbitMQ Vs. Kafka](#redis-vs-rabbitmq-vs-kafka)

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
