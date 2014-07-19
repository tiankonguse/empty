# /etc/profile:此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置.此文件默认调用/etc/bash.bashrc文件。
#
#/etc/bashrc:为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.
#
#~/.bash_profile:每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该
#文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.
#
#~/.bashrc:该文件包含专用于你的bash shell的bash信息。
#
#~/.bash_logout:当每次退出系统(退出bash shell)时,执行该文件. 


# \u  user
# \h  hostname
# \W 当前目录名
# \w 路径名
# 

# 配色
# 颜色的设置，放在相应的要设置的前面
# 前景              背景              颜色
# 30                40               黑色
# 31                41               紅色
# 32                42               綠色
# 33                43               黃色
# 34                44               藍色
# 35                45               紫紅色
# 36                46               青藍色
# 37                47               白色
#           1                         透明色
#
#代码             意义
# 0                 OFF
# 1                 高亮显示
# 4                 underline
# 5                 闪烁
# 7                 反白显示
# 8                 不可见
#

# 一个单独的颜色设置:   \[\033[代码;前景;背景m\ePS1='${debian_chroot:+($debian_chroot)}\[\033[01;04;32m\]\u\[\033[00m\]:\[\033[01;37m\]\W\[\033[31m\]\$ \[\033[00m\]'
#

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;35;40m\]\u\[\033[00;00;40m\]@\[\033[01;35;40m\]\h\[\033[00;31;40m\]:\[\033[00;00;40m\]\W \[\033[01;32;40m\]\$ \[\033[01;36;40m\]'
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;04;32m\]\u\[\033[00m\]:\[\033[01;37m\]\W\[\033[31m\]\$ \[\033[00m\]'


# 对命令重新进行映射
alias vi=vim

# Interactive operation...
 alias rm='rm -i'
 alias cp='cp -i'
 alias mv='mv -i'


# Default to human readable figures
 alias df='df -h'
 alias du='du -h'


# Misc :)
 alias less='less -r'                          # raw control characters
 alias whence='type -a'                        # where, of a sort
 alias grep='grep --color'                     # show differences in colour

alias grep 'gnu grep -i --color=auto'
 alias egrep='egrep --color=auto'              # show differences in colour
 alias fgrep='fgrep --color=auto'              # show differences in colour


# Some shortcuts for different directory listings
 alias ls='ls -hF --color=tty'                 # classify files in colour
 alias dir='ls --color=auto --format=vertical'
 alias vdir='ls --color=auto --format=long'
 alias ll='ls -l'                              # long list
 alias la='ls -A'                              # all but . and ..
 alias l='ls -CF'                              #


c_1="\[\e[0m\]"  #颜色重置
c0="\[\e[30m\]"  #黑色
c1="\[\e[31m\]"  #红色
c2="\[\e[32m\]"  #绿色
c3="\[\e[33m\]"  #l深黄色
c4="\[\e[34m\]"  #蓝色
c5="\[\e[35m\]"  #紫色
c6="\[\e[36m\]"  #湖蓝色
c7="\[\e[37m\]"  #淡灰色









