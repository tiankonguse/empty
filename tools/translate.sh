#########################################################################
# File Name: translate.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: 2014年06月12日 星期四 18时35分59秒
#########################################################################
#!/bin/bash
translate () {
    lang="zh"; 
    text=$*; 
    wget -U "Mozilla/5.0" -qO - "http://translate.google.com/translate_a/t?client=t&text=$text&sl=auto&tl=$lang" | sed 's/\[\[\[\"//' | cut -d \" -f 1;
}
