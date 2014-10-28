#########################################################################
# File Name: dif_rand.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Thu Jul 17 16:37:13 2014
#########################################################################
#!/bin/bash
#产生指定数量的不相同的随机数
#如果未指定数量，默认产生一个。

function usage(){
    echo "usage : difrand num [max_value]";
    echo "creat num different numbers.";
    echo "    num        the number of rand num";
    echo "    max_value  the max value of the rand num. max_value should be more than num";
    echo "               if max_value < num, the value of max_value will be num";
    echo "               by default, max_value is (101 + 3)*7";
}

if (( $# < 1 )) || (( $# > 2 ));
then
    usage;
    exit;
fi

declare -i randnum;
declare -i basenum;

if [[ $1 =~ ^[1-9][0-9]*$ ]]; 
then
    randnum=$1;
else
    usage;
    exit;
fi



if (( $# == 1 ));
then
    basenum=$(( (randnum + 3 )*7 ));
else
    if [[ $2 =~ ^[1-9][0-9]*$ ]] && (( $2 >= $randnum )); 
    then
        basenum=$2;
    else
        usage;
        exit;
    fi
fi

echo $(seq $basenum | shuf | head -n $randnum);
