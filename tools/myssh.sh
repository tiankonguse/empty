#########################################################################
# File Name: ssh.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Thu 27 Feb 2014 11:50:04 AM CST
#########################################################################
#!/bin/bash

select=$1;

declare -i nameNum;
nameNum=0;

# declare show name
declare -a names;

# declare command name 
declare -a commands;


function addSsh(){
    names[$nameNum]=$1;
    commands[$nameNum]=$2;
    nameNum=$(($nameNum+1));
}

function addAll(){
    addSsh "ms" "ssh tiankonguse@23.98.41.103";
    addSsh "msProxy" "ssh -D 7070 tiankonguse@tiankonguse.com";
    addSsh "new ms" "ssh tiankonguse@itworks.cloudapp.net";
    addSsh "new ms free all" "ssh weplay@weplay.cloudapp.net";
    addSsh "new ms free tiankonguse" "ssh tiankonguse@weplay.cloudapp.net";
    addSsh "new ms free vici" "ssh vici@vici.tiankonguse.com";
}

addAll;

#names[0]="ms";
#names[1]="msProxy";
#names[2]="new ms";
#names[3]="new ms free all";
#names[4]="new ms free tiankonguse";
#names[5]="new ms free vici";
#commands[0]="ssh tiankonguse@23.98.41.103";
#commands[1]="ssh -D 7070 tiankonguse@tiankonguse.com";
#commands[2]="ssh tiankonguse@itworks.cloudapp.net";
#commands[3]="ssh weplay@weplay.cloudapp.net";
#commands[4]="ssh tiankonguse@weplay.cloudapp.net";
#commands[5]="ssh vici@vici.tiankonguse.com";

#nameNum=${#names[@]};

function usage(){
    echo "pleace select a number that you want to connect.";
    i=0;

    while [ $i -lt $nameNum ];
    do
        echo "$i :  ${names[$i]}";
        i=$(($i+1));
    done
}


usage;



read i;

if [[ $i =~ ^[0-9]+$ ]]&&[[ $i < $nameNum ]]
then
    eval ${commands[$i]};
    exit;
else
    echo "input error!";
    usage;
fi



