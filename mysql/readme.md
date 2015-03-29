# mysql  学习记录


## 性能优化

mysql 5.1 版本滞后,就自带一些查询工具.


```
mysql> show databases;
+----------------------+
| Database             |
+----------------------+
| information_schema   |
| d_google_code_backup |
| mysql                |
| performance_schema   |
| phpmyadmin           |
+----------------------+
5 rows in set (0.07 sec)
```

### PROFIE

默认 profile 是关闭的.  

```
mysql> select * from t_user where c_name like '%google%' limit 20,10;
+------+------------------------+----------------+---------------+------+
| c_id | c_name                 | c_projects_num | c_starred_num | c_ok |
+------+------------------------+----------------+---------------+------+
| 1527 | augie@google.com       |              0 |             0 |    0 |
| 1584 | davidthorpe@google.com |              0 |             0 |    0 |
| 1621 | georgekeith@google.com |              0 |             0 |    0 |
| 1654 | cthurau@googlemail.com |              0 |             0 |    0 |
| 2012 | rnk@google.com         |              0 |             0 |    0 |
| 2132 | drfibonacci@google.com |              0 |             0 |    0 |
| 2135 | jgw@google.com         |              0 |             0 |    0 |
| 2141 | rdayal@google.com      |              0 |             0 |    0 |
| 2144 | scottb@google.com      |              0 |             0 |    0 |
| 2159 | doog@google.com        |              0 |             0 |    0 |
+------+------------------------+----------------+---------------+------+
10 rows in set (0.00 sec)

mysql> show profiles;
Empty set (0.00 sec)
```


我们需要先打开这个开关.  

然后就可以看到我们的查询流水了.  
默认三个信息:查询id, 查询时间, 查询语句.  
查询事时间精度也很高,精确到微妙了.  



```
mysql> set profiling = 1;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from t_prj_lable where c_prj_name like "%p%" limit 10000, 10;
+------------------+--------------+
| c_prj_name       | c_lable_name |
+------------------+--------------+
| split-lossless   | audio        |
| split-lossless   | tags         |
| imap2signal-spam | script       |
| imap2signal-spam | SignalSpam   |
| imap2signal-spam | IMAP         |
| imap2signal-spam | Perl         |
| imap2signal-spam | junk         |
| headlines-script | script       |
| headlines-script | eggdrop      |
| headlines-script | Tcl          |
+------------------+--------------+
10 rows in set (0.02 sec)

mysql> show profiles;
+----------+------------+-----------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                       |
+----------+------------+-----------------------------------------------------------------------------+
|       10 | 0.14299050 | select * from t_prj_lable where c_prj_name like "%android%" limit 10000, 10 |
|       11 | 0.14190400 | select * from t_prj_lable where c_prj_name like "%android%" limit 5000, 10  |
|       12 | 0.13635350 | select * from t_prj_lable where c_prj_name like "%python%" limit 5000, 10   |
|       13 | 0.09497925 | select * from t_prj_lable where c_prj_name like "%py%" limit 5000, 10       |
|       14 | 0.13439525 | select * from t_prj_lable where c_prj_name like "%py%" limit 50000, 10      |
|       15 | 0.13972650 | select * from t_prj_lable where c_prj_name like "%py%" limit 10000, 10      |
|       16 | 0.11175675 | select * from t_prj_lable where c_prj_name like "%py%" limit 6000, 10       |
|       17 | 0.01420625 | select * from t_prj_lable where c_prj_name like "%p%" limit 6000, 10        |
|       18 | 0.06942050 | select * from t_prj_lable where c_prj_name like "%p%" limit 60000, 10       |
|       19 | 0.13710650 | select * from t_prj_lable where c_prj_name like "%cpp%" limit 60000, 10     |
|       20 | 0.13872950 | select * from t_prj_lable where c_prj_name like "%py%" limit 60000, 10      |
|       21 | 0.00013125 | select * from t_prj_lable where c_prj_name like "%py%" limit 10000, 10      |
|       22 | 0.14147325 | select * from t_prj_lable where c_prj_name like "%py%" limit 8000, 10       |
|       23 | 0.00011650 | select * from t_prj_lable where c_prj_name like "%py%" limit 5000, 10       |
|       24 | 0.01606275 | select * from t_prj_lable where c_prj_name like "%p%" limit 10000, 10       |
+----------+------------+-----------------------------------------------------------------------------+
15 rows in set (0.00 sec)

```

有了 Query\_ID, 我们就可以针对这个 id 查看更详细的信息了.  

```
mysql> show profile for query 24;
+--------------------------------+----------+
| Status                         | Duration |
+--------------------------------+----------+
| starting                       | 0.000025 |
| Waiting for query cache lock   | 0.000006 |
| checking query cache for query | 0.000066 |
| checking permissions           | 0.000009 |
| Opening tables                 | 0.000024 |
| System lock                    | 0.000011 |
| Waiting for query cache lock   | 0.000050 |
| init                           | 0.000031 |
| optimizing                     | 0.000013 |
| statistics                     | 0.000015 |
| preparing                      | 0.000016 |
| executing                      | 0.000004 |
| Sending data                   | 0.015742 |
| end                            | 0.000008 |
| query end                      | 0.000005 |
| closing tables                 | 0.000005 |
| freeing items                  | 0.000005 |
| Waiting for query cache lock   | 0.000002 |
| freeing items                  | 0.000020 |
| Waiting for query cache lock   | 0.000002 |
| freeing items                  | 0.000002 |
| storing result in query cache  | 0.000002 |
| logging slow query             | 0.000002 |
| cleaning up                    | 0.000002 |
+--------------------------------+----------+
24 rows in set (0.00 sec)
```

我们可以看到对于这个查询语句,各个步骤的查询时间.  

而且可以看到 Sending Data 浪费了很多时间,多四个数量级别.  

当然,由于这个列表的字段实际上有很多的,所以我们需要将数据转换为图表或者挑选出最大的哪几个字段比较好.  


### STATUS

```
mysql> show status where variable_name like '%data%';
+-------------------------------+----------+
| Variable_name                 | Value    |
+-------------------------------+----------+
| Com_show_databases            | 0        |
| Com_stmt_send_long_data       | 0        |
| Innodb_buffer_pool_pages_data | 1991     |
| Innodb_buffer_pool_bytes_data | 32620544 |
| Innodb_data_fsyncs            | 7        |
| Innodb_data_pending_fsyncs    | 0        |
| Innodb_data_pending_reads     | 0        |
| Innodb_data_pending_writes    | 0        |
| Innodb_data_read              | 34820096 |
| Innodb_data_reads             | 2002     |
| Innodb_data_writes            | 7        |
| Innodb_data_written           | 35328    |
+-------------------------------+----------+
12 rows in set (0.00 sec)

```

### PROCESSLIST


使用 `show processlist` 命令可以查询正在执行的sql语句.  


```
mysql> show processlist;
+----+------+-----------------+--------------------+---------+------+-------+------------------+
| Id | User | Host            | db                 | Command | Time | State | Info             |
+----+------+-----------------+--------------------+---------+------+-------+------------------+
| 50 | root | localhost:47353 | performance_schema | Query   |    0 | NULL  | show processlist |
+----+------+-----------------+--------------------+---------+------+-------+------------------+
1 row in set (0.00 sec)

```


默认一行一条数据,最后价加个 `\G` 参数,可以试输出一列位一条数据.  

```
mysql> show processlist \G;
*************************** 1. row ***************************
     Id: 50
   User: root
   Host: localhost:47353
     db: performance_schema
Command: Query
   Time: 0
  State: NULL
   Info: show processlist
1 row in set (0.00 sec)

```


其中, state 列很有用的.  
一般有 "freeing items", "end", "cleaning up" 和 "logging slow query".  


### 慢查询日志

要记录所有的日志,可以设置慢查询参数long\_query\_time为0.  












