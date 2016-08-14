#########################################################################
# File Name: test.sh
# Author: tiankonguse(skyyuan)
# mail: i@tiankonguse.com
# Created Time: 2015年06月01日 星期一 21时42分40秒
#########################################################################
#!/bin/bash

cd ./1/;
echo `ls -1 | wc -l`;
for img in *; do

    md5Val=$(md5sum $img | sed 's/^\([0-9a-zA-Z]\+\) .*\(\.[0-9a-zA-Z]\+\)$/\1\2/g' ); 
    if [ $img == $md5Val ];
    then
        continue;
    fi
    mv -f $img $md5Val;
done
echo `ls -1 | wc -l`;
