#########################################################################
# File Name: startWifi.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Sun 18 May 2014 08:47:10 AM CST
#########################################################################
#!/bin/bash

# create 
# iwconfig eth1 essid "***" key s:"***" mode ad-hoc
# ifconfig eth1 192.168.0.1 up
#

# config
# sudo vi /etc/sysctl.conf 
# 取消注释net.ipv4.ip_forward = 1
#
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE


sudo /etc/init.d/networking restart

