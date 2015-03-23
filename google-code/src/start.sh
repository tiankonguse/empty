#########################################################################
# File Name: start.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2015年03月22日 星期日 09时04分08秒
#########################################################################
#!/bin/bash


NUM=`ps -ef | grep "./download_lable.py run" | grep -v grep  | wc -l`

echo `date +"%F %T"`

if [ $NUM -eq 0 ];
then
    echo "start again";
    ./download_lable.py run >> ../log/download_lable.log 2>&1 &
fi


