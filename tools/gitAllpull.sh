#########################################################################
# File Name: gitpull.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2015年03月30日 星期一 21时43分35秒
#########################################################################
#!/bin/bash

function _exe(){
    cmd="$1"
    echo "==>$cmd";
    eval $cmd;
}

function _pull(){
    _exe "git pull origin master";
}

function pull(){
    dir="$1"
    _exe "cd $dir"
    _pull;
   _exe "cd ..;"
}

function main(){
    for dir in ./*
    do
        if [[ -d $dir ]]; 
        then
            pull $dir;
        fi
    done

}

main;
