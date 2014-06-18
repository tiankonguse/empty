#########################################################################
# File Name: gitpush.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月14日 星期六 19时12分40秒
#########################################################################
#!/bin/bash

function _add(){
    git add -A;
    return 0;
}

function _commit(){
    cmd="git commit -m \"$1\"";
    eval $cmd;
    #git commit -m `$1`;
    return 0;
}

function _push(){
    git push origin $1;
    return 0;
}


function _getUpdate(){
    varname="$1";
    l=${#varname};
    if [ "$l" -eq "0" ];
    then
        varname="update";
    fi
    echo "$varname";
}


varmaster="master";

varupdate=$(_getUpdate "$1");

_add;

_commit "$varupdate";

_push "$varmaster";

