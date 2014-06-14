#########################################################################
# File Name: rmNoExFile.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月13日 星期五 15时57分00秒
#########################################################################
#!/bin/bash
ls -1p | grep "^[^./]*$" | xargs rm
