#########################################################################
# File Name: qssh.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Wed Jul 16 14:20:28 2014
#########################################################################
#!/bin/bash

ini_path="$HOME/qssh.ini";

declare -a content;
declare -a content_num;
declare -a head;
declare -a head_num;

function check_ini(){
    if [ -f "$1" ]; then
        return 0;
    else
        return 1;
    fi
}

function read_ini(){
    content=$(cat "$1");
    
    content_num=$(echo -e "$content" | sed -n "$=");

    head=$(echo -e "$content" | grep "\[" | sed "s/^\(\[.*\].*\)$/\1/");
    
    head_num=$(echo -e "$head" | sed -n "$=");
}

function usage(){
    echo "now, there has $head_num server.";
    
    echo "please input the index of server at the head of allow lines.";
    local head_str; 
    head_str=$(echo -e "$head" | awk '{ print FNR " : " $0 }');

    echo "0 : exit";
    echo -e "$head_str";
    echo "q : exit";

    return 0;            
}

function get_end_line(){
    local i;
    local head_name;
    local line;

    i="$1";
    if [[ $i -eq $head_num ]]; then
        echo  "$content_num";
        return;
    fi
    ((i++)); 
    head_name=$(echo -e "$head" | sed -n "${i}p" | sed "s/^\[\(.*\)\].*$/\1/");
    line=$(echo -e "$content" | sed -n "/\[${head_name}\]/=");
    ((line--));
    echo "$line";
}

function connect(){
    local i;
    local head_name;
    local begin_line;
    local end_line;
    local password;
    local username;
    local port;
    local hostname;

    i="$1";
    head_name=$(echo -e "$head" | sed -n "${i}p" | sed "s/^\[\(.*\)\].*$/\1/");

    echo "you select the $i : $head_name server";
    echo "now,begin connect the server...";
    
    begin_line=$(echo -e "$content" | sed -n "/\[${head_name}\]/=");
    end_line=$(get_end_line "$i");
    ((begin_line++));
    local line_str;
    while (( begin_line <= end_line));
    do 
        line_str=$(echo -e "$content" | sed -n "${begin_line}p" | sed "s/^\([^=]\+\)=\(.\+\)$/\1='\2'/" | grep "=");
        if [[ -n $line_str ]];
        then
            eval $line_str; 
        fi
        ((begin_line++));
    done
    expectssh "$username" "$hostname" "$port" "$password";
}

# check init file 
check_ini "$ini_path";
ret=$?;
if [ $ret -ne 0 ]; then
    echo "~/qssh.ini file not exits.";
    exit;
fi

# read ini file config
read_ini "$ini_path";

# help doc
usage;

declare -a i;

while true
do
    read i;

    # exit
    if [[ "_"$i == "_q" ]] || [[ "_"$i == "_0" ]] ;
    then
        exit;
    fi

    # select
    if [[ $i =~ ^[0-9]+$ ]] && (( $i <= $head_num )) && (( $i >= 1 )) ;
    then
        connect "$i";
        exit;
    else
        echo "input error!";
        usage;
    fi
done
