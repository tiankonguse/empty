#########################################################################
# File Name: startAndroid.sh
# Author: tiankonguse
# mail: i@tiankonguse.com
# Created Time: Fri 16 May 2014 09:29:48 PM CST
#########################################################################
#!/bin/bash 

cd /home/tiankonguse/app/android-studio/sdk/platform-tools/;
sudo ./adb kill-server
sudo ./adb devices


