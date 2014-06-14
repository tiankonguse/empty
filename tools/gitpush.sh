#########################################################################
# File Name: gitpush.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月14日 星期六 19时12分40秒
#########################################################################
#!/bin/bash

function add(){
    $(git add -A);
    return 0;
}

function commit(){
    $(git commit -m $1);
    return 0;
}

function push(){
    $(git push orign $1);
    return 0;
}

pwd;
add;
commit "update";
push "master";

