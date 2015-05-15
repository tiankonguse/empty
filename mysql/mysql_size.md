# 查看mysql的各种大小

## 查看所有库的大小

```
select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from information_schema.TABLES;
```

## 查看指定库的大小

```
select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from TABLES where information_schema.table_schema='db';
```

## 查看指定库的指定表的大小

```
select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data  from information_schema.TABLES where table_schema='db' and table_name='table'
```

## 查看指定库的索引大小

```
SELECT CONCAT(ROUND(SUM(index_length)/(1024*1024), 2), ' MB') AS 'Total Index Size' FROM information_schema.TABLES  WHERE table_schema = 'db';
```

## 查看指定库的指定表的索引大小

```
SELECT CONCAT(ROUND(SUM(index_length)/(1024*1024), 2), ' MB') AS 'Total Index Size' FROM information_schema.TABLES  WHERE table_schema = 'db' and table_name='table'; 
```


## 查看一个库中的情况

```
SELECT CONCAT(table_schema,'.',table_name) AS 'Table Name', CONCAT(ROUND(table_rows/1000000,4),'M') AS 'Number of Rows', CONCAT(ROUND(data_length/(1024*1024*1024),4),'G') AS 'Data Size', CONCAT(ROUND(index_length/(1024*1024*1024),4),'G') AS 'Index Size', CONCAT(ROUND((data_length+index_length)/(1024*1024*1024),4),'G') AS'Total'FROM information_schema.TABLES WHERE table_schema LIKE 'test';
```

