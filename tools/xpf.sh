#########################################################################
# File Name: xpf.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年07月16日 12:54:07
#########################################################################
#!/bin/bash

# 打开文件或文件夹，并选中的脚本

cygwin=false;
case "`uname`" in
    CYGWIN*) cygwin=true ;;
esac
 
if [ "$1" = "" ]; then
    XPATH=. # 缺省是当前目录
else
    XPATH=$1
    if $cygwin; then
        XPATH="$(cygpath -C ANSI -w "$XPATH")";
    fi
fi
 
explorer '/select,' $XPATH
