#########################################################################
# File Name: gitpush.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月14日 星期六 19时12分40秒
#########################################################################
#!/bin/bash

function add(){
    cmd="git add -A";
    echo $cmd;
    $cmd;
    return 0;
}

function commit(){
    cmd="git commit -m \"$1\"";
    echo $cmd;
    $cmd;
    return 0;
}

function push(){
    cmd="git push origin $1";
    echo $cmd;
    $cmd;
    return 0;
}


function getUpdate(){
    varname=$1;
    update=${varname:-"update"};
    echo "$update";
    return 0;
}

function getMaster(){
    varname=$1;
    update=${varname:-"master"};
    echo "$update";
}

varupdate=$(getUpdate $1);
varmaster=$(getMaster $2);

echo $varupdate;

add;
commit "$varupdate";
push "$varmaster";

