# Redis commands time complexity cheat sheet

Contents are totally crawled from https://redis.io/commands.

Grouped by command type and ordered by time complexity.

## Regular



| Group | Command | Time Complexity |
| :--- | :--- | :--- |
| cluster | [cluster keyslot](https://redis.io/commands/cluster-keyslot) | O(N) |
| cluster | [cluster reset](https://redis.io/commands/cluster-reset) | O(N) |
| cluster | [cluster delslots](https://redis.io/commands/cluster-delslots) | O(N) |
| cluster | [cluster nodes](https://redis.io/commands/cluster-nodes) | O(N) |
| cluster | [cluster count-failure-reports](https://redis.io/commands/cluster-count-failure-reports) | O(N) |
| cluster | [cluster addslots](https://redis.io/commands/cluster-addslots) | O(N) |
| cluster | [cluster slots](https://redis.io/commands/cluster-slots) | O(N) |
| cluster | [cluster getkeysinslot](https://redis.io/commands/cluster-getkeysinslot) | O(log(N)) |
| cluster | [cluster meet](https://redis.io/commands/cluster-meet) | O(1) |
| cluster | [cluster failover](https://redis.io/commands/cluster-failover) | O(1) |
| cluster | [cluster forget](https://redis.io/commands/cluster-forget) | O(1) |
| cluster | [cluster countkeysinslot](https://redis.io/commands/cluster-countkeysinslot) | O(1) |
| cluster | [cluster info](https://redis.io/commands/cluster-info) | O(1) |
| cluster | [cluster saveconfig](https://redis.io/commands/cluster-saveconfig) | O(1) |
| cluster | [cluster replicate](https://redis.io/commands/cluster-replicate) | O(1) |
| cluster | [readonly](https://redis.io/commands/readonly) | O(1) |
| cluster | [readwrite](https://redis.io/commands/readwrite) | O(1) |
| cluster | [cluster replicas](https://redis.io/commands/cluster-replicas) | O(1) |
| cluster | [cluster slaves](https://redis.io/commands/cluster-slaves) | O(1) |
| cluster | [cluster set-config-epoch](https://redis.io/commands/cluster-set-config-epoch) | O(1) |
| cluster | [cluster setslot](https://redis.io/commands/cluster-setslot) | O(1) |
| connection | [swapdb](https://redis.io/commands/swapdb) | - |
| connection | [select](https://redis.io/commands/select) | - |
| connection | [quit](https://redis.io/commands/quit) | - |
| connection | [ping](https://redis.io/commands/ping) | - |
| connection | [echo](https://redis.io/commands/echo) | - |
| connection | [auth](https://redis.io/commands/auth) | - |
| generic | [sort](https://redis.io/commands/sort) | O(N+M*log(M)) |
| generic | [touch](https://redis.io/commands/touch) | O(N) |
| generic | [migrate](https://redis.io/commands/migrate) | O(N) |
| generic | [keys](https://redis.io/commands/keys) | O(N) |
| generic | [del](https://redis.io/commands/del) | O(N) |
| generic | [scan](https://redis.io/commands/scan) | O(1) |
| generic | [wait](https://redis.io/commands/wait) | O(1) |
| generic | [unlink](https://redis.io/commands/unlink) | O(1) |
| generic | [type](https://redis.io/commands/type) | O(1) |
| generic | [ttl](https://redis.io/commands/ttl) | O(1) |
| generic | [restore](https://redis.io/commands/restore) | O(1) |
| generic | [rename](https://redis.io/commands/rename) | O(1) |
| generic | [renamenx](https://redis.io/commands/renamenx) | O(1) |
| generic | [pttl](https://redis.io/commands/pttl) | O(1) |
| generic | [persist](https://redis.io/commands/persist) | O(1) |
| generic | [pexpireat](https://redis.io/commands/pexpireat) | O(1) |
| generic | [move](https://redis.io/commands/move) | O(1) |
| generic | [object](https://redis.io/commands/object) | O(1) |
| generic | [pexpire](https://redis.io/commands/pexpire) | O(1) |
| generic | [randomkey](https://redis.io/commands/randomkey) | O(1) |
| generic | [expireat](https://redis.io/commands/expireat) | O(1) |
| generic | [exists](https://redis.io/commands/exists) | O(1) |
| generic | [dump](https://redis.io/commands/dump) | O(1) |
| generic | [expire](https://redis.io/commands/expire) | O(1) |
| geo | [georadiusbymember](https://redis.io/commands/georadiusbymember) | O(N+log(M)) |
| geo | [georadius](https://redis.io/commands/georadius) | O(N+log(M)) |
| geo | [geodist](https://redis.io/commands/geodist) | O(log(N)) |
| geo | [geohash](https://redis.io/commands/geohash) | O(log(N)) |
| geo | [geopos](https://redis.io/commands/geopos) | O(log(N)) |
| geo | [geoadd](https://redis.io/commands/geoadd) | O(log(N)) |
| hash | [hvals](https://redis.io/commands/hvals) | O(N) |
| hash | [hmset](https://redis.io/commands/hmset) | O(N) |
| hash | [hgetall](https://redis.io/commands/hgetall) | O(N) |
| hash | [hkeys](https://redis.io/commands/hkeys) | O(N) |
| hash | [hmget](https://redis.io/commands/hmget) | O(N) |
| hash | [hdel](https://redis.io/commands/hdel) | O(N) |
| hash | [hscan](https://redis.io/commands/hscan) | O(1) |
| hash | [hstrlen](https://redis.io/commands/hstrlen) | O(1) |
| hash | [hsetnx](https://redis.io/commands/hsetnx) | O(1) |
| hash | [hlen](https://redis.io/commands/hlen) | O(1) |
| hash | [hexists](https://redis.io/commands/hexists) | O(1) |
| hash | [hincrby](https://redis.io/commands/hincrby) | O(1) |
| hash | [hget](https://redis.io/commands/hget) | O(1) |
| hash | [hincrbyfloat](https://redis.io/commands/hincrbyfloat) | O(1) |
| hash | [hset](https://redis.io/commands/hset) | O(1) |
| hyperloglog | [pfmerge](https://redis.io/commands/pfmerge) | O(N) |
| hyperloglog | [pfcount](https://redis.io/commands/pfcount) | O(1) |
| hyperloglog | [pfadd](https://redis.io/commands/pfadd) | O(1) |
| list | [lrange](https://redis.io/commands/lrange) | O(S+N) |
| list | [ltrim](https://redis.io/commands/ltrim) | O(N) |
| list | [lset](https://redis.io/commands/lset) | O(N) |
| list | [linsert](https://redis.io/commands/linsert) | O(N) |
| list | [lindex](https://redis.io/commands/lindex) | O(N) |
| list | [lrem](https://redis.io/commands/lrem) | O(N) |
| list | [rpushx](https://redis.io/commands/rpushx) | O(1) |
| list | [rpush](https://redis.io/commands/rpush) | O(1) |
| list | [rpop](https://redis.io/commands/rpop) | O(1) |
| list | [rpoplpush](https://redis.io/commands/rpoplpush) | O(1) |
| list | [lpushx](https://redis.io/commands/lpushx) | O(1) |
| list | [lpush](https://redis.io/commands/lpush) | O(1) |
| list | [lpop](https://redis.io/commands/lpop) | O(1) |
| list | [llen](https://redis.io/commands/llen) | O(1) |
| list | [brpoplpush](https://redis.io/commands/brpoplpush) | O(1) |
| list | [brpop](https://redis.io/commands/brpop) | O(1) |
| list | [blpop](https://redis.io/commands/blpop) | O(1) |
| pubsub | [punsubscribe](https://redis.io/commands/punsubscribe) | O(N+M) |
| pubsub | [publish](https://redis.io/commands/publish) | O(N+M) |
| pubsub | [unsubscribe](https://redis.io/commands/unsubscribe) | O(N) |
| pubsub | [subscribe](https://redis.io/commands/subscribe) | O(N) |
| pubsub | [pubsub](https://redis.io/commands/pubsub) | O(N) |
| pubsub | [psubscribe](https://redis.io/commands/psubscribe) | O(N) |
| scripting | [script exists](https://redis.io/commands/script-exists) | O(N) |
| scripting | [script flush](https://redis.io/commands/script-flush) | O(N) |
| scripting | [script load](https://redis.io/commands/script-load) | O(N) |
| scripting | [script debug](https://redis.io/commands/script-debug) | O(1) |
| scripting | [script kill](https://redis.io/commands/script-kill) | O(1) |
| scripting | [evalsha](https://redis.io/commands/evalsha) | Depends on the script that is executed |
| scripting | [eval](https://redis.io/commands/eval) | Depends on the script that is executed |
| server | [memory usage](https://redis.io/commands/memory-usage) | O(N) |
| server | [command getkeys](https://redis.io/commands/command-getkeys) | O(N) |
| server | [command info](https://redis.io/commands/command-info) | O(N) |
| server | [command](https://redis.io/commands/command) | O(N) |
| server | [client list](https://redis.io/commands/client-list) | O(N) |
| server | [client kill](https://redis.io/commands/client-kill) | O(N) |
| server | [client unblock](https://redis.io/commands/client-unblock) | O(log N) |
| server | [time](https://redis.io/commands/time) | O(1) |
| server | [config resetstat](https://redis.io/commands/config-resetstat) | O(1) |
| server | [command count](https://redis.io/commands/command-count) | O(1) |
| server | [client pause](https://redis.io/commands/client-pause) | O(1) |
| server | [client getname](https://redis.io/commands/client-getname) | O(1) |
| server | [client setname](https://redis.io/commands/client-setname) | O(1) |
| server | [client reply](https://redis.io/commands/client-reply) | O(1) |
| server | [client id](https://redis.io/commands/client-id) | O(1) |
| server | [sync](https://redis.io/commands/sync) | - |
| server | [slaveof](https://redis.io/commands/slaveof) | - |
| server | [replicaof](https://redis.io/commands/replicaof) | - |
| server | [shutdown](https://redis.io/commands/shutdown) | - |
| server | [slowlog](https://redis.io/commands/slowlog) | - |
| server | [save](https://redis.io/commands/save) | - |
| server | [role](https://redis.io/commands/role) | - |
| server | [memory stats](https://redis.io/commands/memory-stats) | - |
| server | [monitor](https://redis.io/commands/monitor) | - |
| server | [memory purge](https://redis.io/commands/memory-purge) | - |
| server | [memory malloc-stats](https://redis.io/commands/memory-malloc-stats) | - |
| server | [lastsave](https://redis.io/commands/lastsave) | - |
| server | [memory doctor](https://redis.io/commands/memory-doctor) | - |
| server | [memory help](https://redis.io/commands/memory-help) | - |
| server | [flushdb](https://redis.io/commands/flushdb) | - |
| server | [flushall](https://redis.io/commands/flushall) | - |
| server | [debug segfault](https://redis.io/commands/debug-segfault) | - |
| server | [debug object](https://redis.io/commands/debug-object) | - |
| server | [dbsize](https://redis.io/commands/dbsize) | - |
| server | [config set](https://redis.io/commands/config-set) | - |
| server | [config rewrite](https://redis.io/commands/config-rewrite) | - |
| server | [config get](https://redis.io/commands/config-get) | - |
| server | [bgsave](https://redis.io/commands/bgsave) | - |
| server | [bgrewriteaof](https://redis.io/commands/bgrewriteaof) | - |
| server | [info](https://redis.io/commands/info) | - |
| set | [sinterstore](https://redis.io/commands/sinterstore) | O(N*M) |
| set | [sinter](https://redis.io/commands/sinter) | O(N*M) |
| set | [sunion](https://redis.io/commands/sunion) | O(N) |
| set | [sunionstore](https://redis.io/commands/sunionstore) | O(N) |
| set | [srem](https://redis.io/commands/srem) | O(N) |
| set | [smembers](https://redis.io/commands/smembers) | O(N) |
| set | [sdiff](https://redis.io/commands/sdiff) | O(N) |
| set | [sdiffstore](https://redis.io/commands/sdiffstore) | O(N) |
| set | [sscan](https://redis.io/commands/sscan) | O(1) |
| set | [spop](https://redis.io/commands/spop) | O(1) |
| set | [sismember](https://redis.io/commands/sismember) | O(1) |
| set | [srandmember](https://redis.io/commands/srandmember) | O(1) |
| set | [sadd](https://redis.io/commands/sadd) | O(1) |
| set | [scard](https://redis.io/commands/scard) | O(1) |
| set | [smove](https://redis.io/commands/smove) | O(1) |
| sorted_set | [zinterstore](https://redis.io/commands/zinterstore) | O(N*K) |
| sorted_set | [zunionstore](https://redis.io/commands/zunionstore) | O(N) |
| sorted_set | [zrem](https://redis.io/commands/zrem) | O(M*log(N)) |
| sorted_set | [zrevrange](https://redis.io/commands/zrevrange) | O(log(N)+M) |
| sorted_set | [zremrangebyrank](https://redis.io/commands/zremrangebyrank) | O(log(N)+M) |
| sorted_set | [zremrangebyscore](https://redis.io/commands/zremrangebyscore) | O(log(N)+M) |
| sorted_set | [zrevrangebylex](https://redis.io/commands/zrevrangebylex) | O(log(N)+M) |
| sorted_set | [zrangebyscore](https://redis.io/commands/zrangebyscore) | O(log(N)+M) |
| sorted_set | [zremrangebylex](https://redis.io/commands/zremrangebylex) | O(log(N)+M) |
| sorted_set | [zrevrangebyscore](https://redis.io/commands/zrevrangebyscore) | O(log(N)+M) |
| sorted_set | [zrangebylex](https://redis.io/commands/zrangebylex) | O(log(N)+M) |
| sorted_set | [zrange](https://redis.io/commands/zrange) | O(log(N)+M) |
| sorted_set | [zpopmin](https://redis.io/commands/zpopmin) | O(log(N)*M) |
| sorted_set | [zpopmax](https://redis.io/commands/zpopmax) | O(log(N)*M) |
| sorted_set | [zrevrank](https://redis.io/commands/zrevrank) | O(log(N)) |
| sorted_set | [zrank](https://redis.io/commands/zrank) | O(log(N)) |
| sorted_set | [zlexcount](https://redis.io/commands/zlexcount) | O(log(N)) |
| sorted_set | [zincrby](https://redis.io/commands/zincrby) | O(log(N)) |
| sorted_set | [zadd](https://redis.io/commands/zadd) | O(log(N)) |
| sorted_set | [zcount](https://redis.io/commands/zcount) | O(log(N)) |
| sorted_set | [bzpopmax](https://redis.io/commands/bzpopmax) | O(log(N)) |
| sorted_set | [bzpopmin](https://redis.io/commands/bzpopmin) | O(log(N)) |
| sorted_set | [zscan](https://redis.io/commands/zscan) | O(1) |
| sorted_set | [zscore](https://redis.io/commands/zscore) | O(1) |
| sorted_set | [zcard](https://redis.io/commands/zcard) | O(1) |
| stream | [xpending](https://redis.io/commands/xpending) | O(N) |
| stream | [xread](https://redis.io/commands/xread) | O(N) |
| stream | [xrange](https://redis.io/commands/xrange) | O(N) |
| stream | [xtrim](https://redis.io/commands/xtrim) | O(N) |
| stream | [xrevrange](https://redis.io/commands/xrevrange) | O(N) |
| stream | [xinfo](https://redis.io/commands/xinfo) | O(N) |
| stream | [xreadgroup](https://redis.io/commands/xreadgroup) | O(M) |
| stream | [xclaim](https://redis.io/commands/xclaim) | O(log N) |
| stream | [xack](https://redis.io/commands/xack) | O(1) |
| stream | [xlen](https://redis.io/commands/xlen) | O(1) |
| stream | [xadd](https://redis.io/commands/xadd) | O(1) |
| stream | [xdel](https://redis.io/commands/xdel) | O(1) |
| stream | [xgroup](https://redis.io/commands/xgroup) | O(1) |
| string | [msetnx](https://redis.io/commands/msetnx) | O(N) |
| string | [mget](https://redis.io/commands/mget) | O(N) |
| string | [mset](https://redis.io/commands/mset) | O(N) |
| string | [getrange](https://redis.io/commands/getrange) | O(N) |
| string | [bitpos](https://redis.io/commands/bitpos) | O(N) |
| string | [bitop](https://redis.io/commands/bitop) | O(N) |
| string | [bitcount](https://redis.io/commands/bitcount) | O(N) |
| string | [append](https://redis.io/commands/append) | O(1) |
| string | [strlen](https://redis.io/commands/strlen) | O(1) |
| string | [setex](https://redis.io/commands/setex) | O(1) |
| string | [setrange](https://redis.io/commands/setrange) | O(1) |
| string | [setnx](https://redis.io/commands/setnx) | O(1) |
| string | [setbit](https://redis.io/commands/setbit) | O(1) |
| string | [psetex](https://redis.io/commands/psetex) | O(1) |
| string | [incrby](https://redis.io/commands/incrby) | O(1) |
| string | [incrbyfloat](https://redis.io/commands/incrbyfloat) | O(1) |
| string | [incr](https://redis.io/commands/incr) | O(1) |
| string | [getbit](https://redis.io/commands/getbit) | O(1) |
| string | [get](https://redis.io/commands/get) | O(1) |
| string | [getset](https://redis.io/commands/getset) | O(1) |
| string | [set](https://redis.io/commands/set) | O(1) |
| string | [decrby](https://redis.io/commands/decrby) | O(1) |
| string | [decr](https://redis.io/commands/decr) | O(1) |
| string | [bitfield](https://redis.io/commands/bitfield) | O(1) |
| transactions | [watch](https://redis.io/commands/watch) | O(1) |
| transactions | [unwatch](https://redis.io/commands/unwatch) | O(1) |
| transactions | [multi](https://redis.io/commands/multi) | - |
| transactions | [exec](https://redis.io/commands/exec) | - |
| transactions | [discard](https://redis.io/commands/discard) | -| 
