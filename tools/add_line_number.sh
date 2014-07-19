#########################################################################
# File Name: add_line_number.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Thu Jul 17 17:15:01 2014
#########################################################################
#!/bin/bash

# 给文件的前面加一个行号

function usage(){
    echo "usage : addlinenumber filename.";
}


if (( $# == 1));
then
    if [[ -e $1 ]];
    then
        cat "$1" | awk '{ print FNR " " $0}' > "$1";  
    else
        usage;
    fi
else
    usage;
fi

