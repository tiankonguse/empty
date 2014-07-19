#########################################################################
# File Name: ifind.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Thu Jul 17 18:57:16 2014
#########################################################################
#!/bin/bash


if (( $# == 0 ));
then
    echo "usage : ifind string":
    exit;
fi
IFS='|'; 

grep -rinE --color "$*" . ; 
