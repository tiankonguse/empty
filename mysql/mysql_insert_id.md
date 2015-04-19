# mysql　最后插入的记录ID


前段时间，一同事问我怎么得到mysql插入一条记录的ID.  

于是查了一个文档，发现有`mysql_insert_id()`这个函数．  

然后那同事问我，并发下这个获得的ID正确吗?  

我说：mysql大家都在用，而且都是并发使用．应该是正确的，不然这个函数就没有用了吧．  

同事说也是．  

然后我想:虽然是这么说，但是不拿出真实凭证来，还是不可靠的．  

于是查了一下[mysql的官方文档][mysql-refman-mysql-insert-id]．  

然后发现这个一句话：  

```
The value of mysql_insert_id() is affected only by statements issued within the current client connection.   
It is not affected by statements issued by other clients.  
```

简单的说就是 `mysql_insert_id()` 函数只被当前客户端的连接影响，　其他客户端的语句不会影响这个链接的．  



[chinaunix-626134]: http://bbs.chinaunix.net/forum.php?mod=viewthread&action=printable&tid=626134
[JohnABC-3435237]: http://www.cnblogs.com/JohnABC/p/3435237.html
[mysql-refman-mysql-insert-id]: https://dev.mysql.com/doc/refman/5.0/en/mysql-insert-id.html

