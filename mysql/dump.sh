#########################################################################
# File Name: dump.sh
# Author: tiankonguse(skyyuan)
# mail: i@tiankonguse.com
# Created Time: 2015年04月 8日 13:26:48
#########################################################################
#!/bin/bash

$IP=mysql服务器IP
$PORT=端口
$USERNAME=用户名
$PASSWORK=密码
$DB=数据库
$TABLE=表

mysqldump -h${IP} -P${PORT} --single-transaction -u${USERNAME} -p${PASSWORD}  ${DB} --table ${TABLE} >  ${TABLE}.sql

mysql -h${IP} -P${PORT} -u${USERNAME} -p${PASSWORD} ${DB} < ${TABLE}.sql
