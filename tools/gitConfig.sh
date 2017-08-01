#########################################################################
# File Name: gitConfig.sh
# Author: tiankonguse(skyyuan)
# mail: i@tiankonguse.com
# Created Time: 2017年08月 1日 10:39:46
#########################################################################
#!/bin/bash

git config --global user.name "tiankonguse"
git config --global user.email "i@tiankonguse.com"
git config --global credential.helper 'cache --timeout=3600'


git config --list
