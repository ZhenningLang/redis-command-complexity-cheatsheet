# Redis commands time complexity cheat sheet

Contents are totally crawled from https://redis.io/commands

| Group | Command | TimeComplexity |
| :--- | :--- | :--- |
| Cluster | cluster nodes | O(N) |
|  | cluster keyslot | O(N) |
|  | cluster reset | O(N) |
|  | cluster delslots | O(N) |
|  | cluster count-failure-reports | O(N) |
|  | cluster addslots | O(N) |
|  | cluster slots | O(N) |
|  | cluster getkeysinslot | O(log(N) |
|  | cluster info | O(1) |
|  | cluster replicate | O(1) |
|  | cluster forget | O(1) |
|  | cluster set-config-epoch | O(1) |
|  | cluster meet | O(1) |
|  | cluster saveconfig | O(1) |
|  | cluster failover | O(1) |
|  | cluster countkeysinslot | O(1) |
|  | readwrite | O(1) |
|  | readonly | O(1) |
|  | cluster replicas | O(1) |
|  | cluster setslot | O(1) |
|  | cluster slaves | O(1) |
| connection | swapdb | - |
|  | select | - |
|  | quit | - |
|  | ping | - |
|  | echo | - |
|  | auth | - |
| generic | sort | O(N+M*log(M) |
|  | touch | O(N) |
|  | migrate | O(N) |
|  | keys | O(N) |
|  | del | O(N) |
|  | scan | O(1) |
|  | wait | O(1) |
|  | unlink | O(1) |
|  | ttl | O(1) |
|  | type | O(1) |
|  | renamenx | O(1) |
|  | restore | O(1) |
|  | rename | O(1) |
|  | randomkey | O(1) |
|  | pttl | O(1) |
|  | pexpireat | O(1) |
|  | pexpire | O(1) |
|  | object | O(1) |
|  | persist | O(1) |
|  | move | O(1) |
|  | expireat | O(1) |
|  | expire | O(1) |
|  | exists | O(1) |
|  | dump | O(1) |
| geo | georadiusbymember | O(N+log(M) |
|  | georadius | O(N+log(M) |
|  | geodist | O(log(N) |
|  | geoadd | O(log(N) |
|  | geopos | O(log(N) |
|  | geohash | O(log(N) |
| hash | hvals | O(N) |
|  | hmset | O(N) |
|  | hmget | O(N) |
|  | hkeys | O(N) |
|  | hgetall | O(N) |
|  | hdel | O(N) |
|  | hscan | O(1) |
|  | hstrlen | O(1) |
|  | hsetnx | O(1) |
|  | hset | O(1) |
|  | hlen | O(1) |
|  | hincrbyfloat | O(1) |
|  | hget | O(1) |
|  | hincrby | O(1) |
|  | hexists | O(1) |
| hyperloglog | pfmerge | O(N) |
|  | pfcount | O(1) |
|  | pfadd | O(1) |
| list | lrange | O(S+N) |
|  | ltrim | O(N) |
|  | lset | O(N) |
|  | lrem | O(N) |
|  | linsert | O(N) |
|  | lindex | O(N) |
|  | rpushx | O(1) |
|  | rpush | O(1) |
|  | rpop | O(1) |
|  | rpoplpush | O(1) |
|  | llen | O(1) |
|  | lpushx | O(1) |
|  | lpush | O(1) |
|  | lpop | O(1) |
|  | brpop | O(1) |
|  | brpoplpush | O(1) |
|  | blpop | O(1) |
| pubsub | punsubscribe | O(N+M) |
|  | publish | O(N+M) |
|  | unsubscribe | O(N) |
|  | subscribe | O(N) |
|  | pubsub | O(N) |
|  | psubscribe | O(N) |
| scripting | script load | O(N) |
|  | script flush | O(N) |
|  | script exists | O(N) |
|  | script kill | O(1) |
|  | script debug | O(1) |
|  | evalsha | https://redis.io/commands/evalsha |
|  | eval | https://redis.io/commands/eval |
| server | memory usage | O(N) |
|  | command info | O(N) |
|  | command getkeys | O(N) |
|  | command | O(N) |
|  | client list | O(N) |
|  | client kill | O(N) |
|  | client unblock | O(log N) |
|  | time | O(1) |
|  | config resetstat | O(1) |
|  | command count | O(1) |
|  | client setname | O(1) |
|  | client getname | O(1) |
|  | client reply | O(1) |
|  | client pause | O(1) |
|  | client id | O(1) |
|  | sync | - |
|  | slowlog | - |
|  | replicaof | - |
|  | slaveof | - |
|  | shutdown | - |
|  | save | - |
|  | role | - |
|  | monitor | - |
|  | memory stats | - |
|  | memory purge | - |
|  | memory malloc-stats | - |
|  | memory help | - |
|  | memory doctor | - |
|  | lastsave | - |
|  | info | - |
|  | flushdb | - |
|  | flushall | - |
|  | config set | - |
|  | debug segfault | - |
|  | debug object | - |
|  | dbsize | - |
|  | config rewrite | - |
|  | config get | - |
|  | bgsave | - |
|  | bgrewriteaof | - |
| set | sinterstore | O(N*M) |
|  | sinter | O(N*M) |
|  | sunionstore | O(N) |
|  | sunion | O(N) |
|  | srem | O(N) |
|  | smembers | O(N) |
|  | sdiffstore | O(N) |
|  | sdiff | O(N) |
|  | sscan | O(1) |
|  | srandmember | O(1) |
|  | spop | O(1) |
|  | smove | O(1) |
|  | sismember | O(1) |
|  | scard | O(1) |
|  | sadd | O(1) |
| sorted_set | zinterstore | O(N*K) |
|  | zunionstore | O(N) |
|  | zrem | O(M*log(N) |
|  | zrevrank | O(log(N) |
|  | zrevrange | O(log(N) |
|  | zrevrangebyscore | O(log(N) |
|  | zremrangebyrank | O(log(N) |
|  | zremrangebylex | O(log(N) |
|  | zrank | O(log(N) |
|  | zremrangebyscore | O(log(N) |
|  | zrangebyscore | O(log(N) |
|  | zrangebylex | O(log(N) |
|  | zrevrangebylex | O(log(N) |
|  | zrange | O(log(N) |
|  | zpopmin | O(log(N) |
|  | zpopmax | O(log(N) |
|  | zlexcount | O(log(N) |
|  | zincrby | O(log(N) |
|  | zcount | O(log(N) |
|  | zadd | O(log(N) |
|  | bzpopmax | O(log(N) |
|  | bzpopmin | O(log(N) |
|  | zscan | O(1) |
|  | zscore | O(1) |
|  | zcard | O(1) |
| stream | xpending | O(N) |
|  | xread | O(N) |
|  | xrevrange | O(N) |
|  | xtrim | O(N) |
|  | xrange | O(N) |
|  | xinfo | O(N) |
|  | xreadgroup | O(M) |
|  | xclaim | O(log N) |
|  | xack | O(1) |
|  | xgroup | O(1) |
|  | xdel | O(1) |
|  | xlen | O(1) |
|  | xadd | O(1) |
| string | msetnx | O(N) |
|  | mset | O(N) |
|  | mget | O(N) |
|  | getrange | O(N) |
|  | bitpos | O(N) |
|  | bitop | O(N) |
|  | bitcount | O(N) |
|  | append | O(1) |
|  | strlen | O(1) |
|  | setrange | O(1) |
|  | setex | O(1) |
|  | setbit | O(1) |
|  | set | O(1) |
|  | setnx | O(1) |
|  | psetex | O(1) |
|  | incrbyfloat | O(1) |
|  | incrby | O(1) |
|  | incr | O(1) |
|  | getset | O(1) |
|  | getbit | O(1) |
|  | get | O(1) |
|  | decrby | O(1) |
|  | decr | O(1) |
|  | bitfield | O(1) |
| transactions | watch | O(1) |
|  | unwatch | O(1) |
|  | multi | - |
|  | exec | - |
|  | discard | - |
