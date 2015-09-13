1. 创建用户:

命令:CREATE USER username IDENTIFIED BY 'password';
说明:username——你将创建的用户名, password——该用户的登陆密码,密码可以为空,如果为空则该用户可以不需要密码登陆服务器.
示例:

```
CREATE USER test IDENTIFIED BY 'test';
````



2.授权:

命令:GRANT privileges ON databasename.tablename TO username;
说明:

privileges——用户的操作权限,如SELECT , INSERT , UPDATE 等，如果要授予所有的权限则使用ALL.;
databasename——数据库名；
tablename——表名,如果要授予该用户对所有数据库和表的相应操作权限则可用*表示, 如*.*.
示例: 


```
GRANT SELECT , INSERT , UPDATE, DELETE ON test.test TO test;  
GRANT ALL ON *.* TO ; 
```



