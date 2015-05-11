# mysql 监控命令

## 查看当前连接数

```
SHOW STATUS LIKE 'Thread_%';
Thread_cached:被缓存的线程的个数
Thread_running：处于激活状态的线程的个数
Thread_connected：当前连接的线程的个数
Thread_created：总共被创建的线程的个数
```

## Thread cache hits

```
Thread_connected = SHOW GLOBAL STATUS LIKE Thread_created;
Connections = SHOW GLOBAL STATUS LIKE 'Connections';
TCH=(1 - (Threads_created / Connections)) * 100
```

如果 TCH数小于90%,创建连接耗费了时间,增大Thread\_cached数量

## 查看活动连接内容

```
SHOW PROCESSLIST;
```

## QPS

```
Questions = SHOW GLOBAL STATUS LIKE 'Questions';
Uptime = SHOW GLOBAL STATUS LIKE 'Uptime';
QPS=Questions/Uptime 
```

## TPS

```
Com_commit = SHOW GLOBAL STATUS LIKE 'Com_commit';
Com_rollback = SHOW GLOBAL STATUS LIKE 'Com_rollback';
Uptime = SHOW GLOBAL STATUS LIKE 'Uptime';
TPS=(Com_commit + Com_rollback)/Uptime
```

## Read/Writes Ratio

```
Qcache_hits = SHOW GLOBAL STATUS LIKE 'Qcache_hits';
Com_select = SHOW GLOBAL STATUS LIKE 'Com_select';
Com_insert = SHOW GLOBAL STATUS LIKE 'Com_insert';
Com_update = SHOW GLOBAL STATUS LIKE 'Com_update';
Com_delete = SHOW GLOBAL STATUS LIKE 'Com_delete';
Com_replace = SHOW GLOBAL STATUS LIKE 'Com_replace';
R/W=(Com_select + Qcache_hits) / (Com_insert + Com_update + Com_delete + Com_replace) * 100
```


## Slow queries per minute

```
Slow_queries = SHOW GLOBAL STATUS LIKE 'Slow_queries';
Uptime = SHOW GLOBAL STATUS LIKE 'Uptime';
SQPM=Slow_queries / (Uptime/60)
```

## Slow queries /Questions Ratio

```
Slow_queries = SHOW GLOBAL STATUS LIKE 'Slow_queries';
Questions = SHOW GLOBAL STATUS LIKE 'Questions';
S/Q=Slow_queries/Questions 
```

## Full_join per minute


```
Select_full_join = SHOW GLOBAL STATUS LIKE 'Select_full_join';
Uptime = SHOW GLOBAL STATUS LIKE 'Uptime';
FJPM=Select_full_join / (Uptime/60)
```


## Innodb buffer read hits

```
Innodb_buffer_pool_reads = SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_reads';
Innodb_buffer_pool_read_requests = SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_read_requests';
IFRH=(1 - Innodb_buffer_pool_reads/Innodb_buffer_pool_read_requests) * 100
```

## Table Cache

```
Open_tables= SHOW GLOBAL STATUS LIKE 'Open_tables';
Opened_tables= SHOW GLOBAL STATUS LIKE 'Opened_tables';
table_cache= SHOW GLOBAL STATUS LIKE 'table_cache';
```

## Temp tables to Disk Ratio

```
Created_tmp_tables = show global status like 'Created_tmp_tables';
Created_tmp_disk_tables = show global status like 'Created_tmp_disk_tables';

TDR=(Created_tmp_disk_tables/Created_tmp_tables)*100
```

