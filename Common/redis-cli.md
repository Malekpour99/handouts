# Redis-CLI

## Table of Contents

- [Redis-CLI](#redis-cli)
  - [Table of Contents](#table-of-contents)
  - [Common Commands](#common-commands)
  - [List Operations (Queue-style)](#list-operations-queue-style)
  - [Set Operations](#set-operations)
  - [Hash Operations (like dict/object)](#hash-operations-like-dictobject)
  - [Sorted Set (ranking, leaderboards)](#sorted-set-ranking-leaderboards)
  - [Scan Keys (DON’T use KEYS in production!)](#scan-keys-dont-use-keys-in-production)
  - [Pub/Sub (basic messaging)](#pubsub-basic-messaging)

## Common Commands

```sh
# connect to redis (default localhost:6379)
redis-cli

# connect to remote redis
redis-cli -h <host> -p <port> -a <password>

# check if server is alive
PING

# get server info (memory, clients, etc.)
INFO

# select database (0–15 by default)
SELECT <db_index>

# set a key
SET <key> <value>

# get a key
GET <key>

# delete a key
DEL <key>

# check if key exists
EXISTS <key>

# set key with expiration (seconds)
SETEX <key> <seconds> <value>

# set expiration on existing key
EXPIRE <key> <seconds>

# get remaining ttl
TTL <key>

# remove expiration
PERSIST <key>

# increment integer value
INCR <key>

# increment by specific amount
INCRBY <key> <amount>

# decrement value
DECR <key>

# append to string
APPEND <key> <value>

# get string length
STRLEN <key>
```

## List Operations (Queue-style)

```sh
# push to left
LPUSH <key> <value>

# push to right
RPUSH <key> <value>

# pop from left
LPOP <key>

# pop from right
RPOP <key>

# get list range
LRANGE <key> <start> <end>
```

## Set Operations

```sh
# add to set
SADD <key> <value>

# remove from set
SREM <key> <value>

# get all members
SMEMBERS <key>

# check membership
SISMEMBER <key> <value>
```

## Hash Operations (like dict/object)

```sh
# set field
HSET <key> <field> <value>

# get field
HGET <key> <field>

# get all fields/values
HGETALL <key>

# delete field
HDEL <key> <field>
```

## Sorted Set (ranking, leaderboards)

```sh
# add with score
ZADD <key> <score> <member>

# get by score/rank
ZRANGE <key> <start> <end>

# get with scores
ZRANGE <key> <start> <end> WITHSCORES

# remove member
ZREM <key> <member>
```

## Scan Keys (DON’T use KEYS in production!)

```sh
# iterate keys safely
SCAN 0

# scan with pattern
SCAN 0 MATCH <pattern>

# get key type
TYPE <key>

# rename key
RENAME <old_key> <new_key>

# flush current db (dangerous!)
FLUSHDB

# flush all dbs (VERY dangerous!!)
FLUSHALL

# monitor all commands (debugging, heavy)
MONITOR

# check memory usage of key
MEMORY USAGE <key>
```

## Pub/Sub (basic messaging)

```sh
# subscribe to channel
SUBSCRIBE <channel>

# publish message
PUBLISH <channel> <message>
```
