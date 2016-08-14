#########################################################################
# File Name: gitpush.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月14日 星期六 19时12分40秒
#########################################################################
#!/bin/bash

function _add(){
    cmd="git add -A";
    echo "===>$cmd";
    eval $cmd;
}

function _commit(){
    cmd="git commit -m \"$1\"";
    echo "==＝>$cmd";
    eval $cmd;
}

function _push(){
    cmd="git push origin $1";
    echo "===>$cmd";
    eval $cmd;

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

function _getMaster(){
    varname="$1";
    l=${#varname};
    if [ "$l" -eq "0" ] ;
    then
        varname="master"
    fi
    echo "$varname";
}


function _pull(){
    cmd="git pull origin master";
    echo "===>$cmd";
    eval $cmd;
}

varupdate=$(_getUpdate "$1");

varmaster=$(_getMaster "$2");


_pull;

_add;

_commit "$varupdate";

_push "$varmaster";

_push "--tag";

