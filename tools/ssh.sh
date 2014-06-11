#########################################################################
# File Name: ssh.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Thu 27 Feb 2014 11:50:04 AM CST
#########################################################################
#!/bin/bash

declare -i nameNum;


# declare show name


declare -a names;

names[0]="ms";
names[1]="msProxy";
names[2]="new ms";
names[3]="new ms free all";
names[4]="new ms free tiankonguse";
names[5]="new ms free vici";

nameNum=${#names[@]};

echo "pleace select a number that you want to connect.";

i=0;

while [ $i -lt $nameNum ];
do
    echo "$i :  ${names[$i]}";
    i=$(($i+1));
done


# declare command name 

declare -a commands;

commands[0]="ssh tiankonguse@23.98.41.103";
commands[1]="ssh -D 7070 tiankonguse@tiankonguse.com ";
commands[2]="ssh tiankonguse@itworks.cloudapp.net";
commands[3]="ssh weplay@weplay.cloudapp.net";
commands[4]="ssh tiankonguse@weplay.cloudapp.net";
commands[5]="ssh vici@vici.tiankonguse.com";


read i;

if [[ $i =~ ^[0-9]+$ ]]&&[[ $i < $nameNum ]]
then
    eval ${commands[$i]};
else
    echo "input error!";
fi



