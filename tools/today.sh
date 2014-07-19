#########################################################################
# File Name: today.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Fri Jul 18 11:32:27 2014
#########################################################################
#!/bin/bash

#今天高亮的日历

cal | grep -E --color "\b`date +%e`\b|$"

