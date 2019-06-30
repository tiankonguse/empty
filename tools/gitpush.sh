#########################################################################
# File Name: gitpush.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月14日 星期六 19时12分40秒
#########################################################################
#!/bin/bash

function _ext(){
    #!/bin/bash
set -e

RESET="\033[0m"
REDCOLOR="\033[31m"
GREENCOLOR="\033[32m"

current_branch=`git branch | awk '/\*/ {print $2}'`

clear
echo -e $GREENCOLOR"--------------------------------------- STARTING PUSH -------------------------------------------"$RESET

git checkout master && git pull origin master && git checkout $current_branch && git rebase master && git checkout master && git pull origin master && git merge $current_branch && git push origin master && git checkout $current_branch || {
	echo -e $REDCOLOR"----------------------------------- PUSH FAILED (SEE ERRORS)-------------------------------------"$RESET;
	echo -e $REDCOLOR"---- Most likely, you will just need to run 'git mergetool' and then 'git rebase --continue' ----"$RESET;
	exit 1;
}

echo -e $GREENCOLOR"--------------------------------- PUSH AND REBASE SUCCESSFUL ------------------------------------"$RESET
    
}

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

#_push "--tag";

