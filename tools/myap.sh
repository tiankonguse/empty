#########################################################################
# File Name: myap.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Mon 12 May 2014 05:28:09 PM CST
#########################################################################
#!/bin/sh
#为无线添加路由规则
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE
iptables -A FORWARD -s 192.168.1.0/24 -o eth0 -j ACCEPT
iptables -A FORWARD -d 192.168.1.0/24 -m conntrack --ctstate ESTABLISHED,RELATED -i eth0 -j ACCEPT
