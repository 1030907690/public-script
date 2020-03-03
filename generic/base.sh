#!/bin/bash

platform=`uname -i`
if [ $platform != "x86_64" ];then
echo "this script is only for 64bit Operating System !"
exit 1
fi
echo "the platform is ok"
cat << EOF
+---------------------------------------+
|   your system is CentOS 7 x86_64      |
|      start optimizing.......          |
+---------------------------------------
EOF



yum clean all
yum makecache

# update os or soft
yum update -y
echo y

# man chinese pages
yum install man-pages-zh-CN.noarch  -y
# Conventional tools
yum install ntp wget git tcpdump net-tools -y
yum install vim lrzsz zip unzip epel-release -y
#install jdk-1.8.0-openjdk

timedatectl set-timezone Asia/Shanghai
timedatectl set-local-rtc 1
/usr/sbin/ntpdate cn.pool.ntp.org
echo "* 4 * * * /usr/sbin/ntpdate cn.pool.ntp.org > /dev/null 2>&1" >> /var/spool/cron/root
systemctl  restart crond.service

#yum install java-1.8.0-openjdk* -y
#wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

echo "ulimit -SHn 102400" >> /etc/rc.local
cat >> /etc/security/limits.conf << EOF
*           soft   nofile       655350
*           hard   nofile       655350
*           soft   nproc        655350
*           hard   nproc        655350
EOF


sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
setenforce 0


# Ban ping
#echo "1" > /proc/sys/net/ipv4/icmp_echo_ignore_all

# vim optimization
echo 'alias vi=vim' >> /etc/profile
#echo 'stty erase ^H' >> /etc/profile
cat >> /root/.vimrc << EOF
set tabstop=4
set shiftwidth=4
set expandtab
set helplang=cn
set encoding=utf-8
set fileencodings=ucs-bomo,utf-8,chinese,gbk,latin-1
set ffs=unix,dos,mac
set backspace=indent,eol,start
set whichwrap=b,s,<,>,[,]
set number
EOF

# kernel optimization
cat >> /etc/sysctl.conf << EOF
#CTCDN系统优化参数
#关闭ipv6
#net.ipv6.conf.all.disable_ipv6 = 1
#net.ipv6.conf.default.disable_ipv6 = 1
#决定检查过期多久邻居条目
net.ipv4.neigh.default.gc_stale_time=120
#使用arp_announce / arp_ignore解决ARP映射问题
net.ipv4.conf.default.arp_announce = 2
net.ipv4.conf.all.arp_announce=2
net.ipv4.conf.lo.arp_announce=2
# 避免放大攻击
net.ipv4.icmp_echo_ignore_broadcasts = 1
# 开启恶意icmp错误消息保护
net.ipv4.icmp_ignore_bogus_error_responses = 1
#开启路由转发
net.ipv4.ip_forward = 1
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
#开启反向路径过滤
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
#处理无源路由的包
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
#关闭sysrq功能
kernel.sysrq = 0
#core文件名中添加pid作为扩展名
kernel.core_uses_pid = 1
# 开启SYN洪水攻击保护
net.ipv4.tcp_syncookies = 1
#修改消息队列长度
kernel.msgmnb = 65536
kernel.msgmax = 65536
#设置最大内存共享段大小bytes
kernel.shmmax = 68719476736
kernel.shmall = 4294967296
#timewait的数量，默认180000
net.ipv4.tcp_max_tw_buckets = 6000
net.ipv4.tcp_sack = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_rmem = 4096        87380   4194304
net.ipv4.tcp_wmem = 4096        16384   4194304
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
#每个网络接口接收数据包的速率比内核处理这些包的速率快时，允许送到队列的数据包的最大数目
#net.core.netdev_max_backlog = 262144
#限制仅仅是为了防止简单的DoS 攻击
net.ipv4.tcp_max_orphans = 3276800
#未收到客户端确认信息的连接请求的最大值
net.ipv4.tcp_max_syn_backlog = 262144
net.ipv4.tcp_timestamps = 0
#内核放弃建立连接之前发送SYNACK 包的数量
net.ipv4.tcp_synack_retries = 1
#内核放弃建立连接之前发送SYN 包的数量
net.ipv4.tcp_syn_retries = 1
#启用timewait 快速回收
net.ipv4.tcp_tw_recycle = 1
#开启重用。允许将TIME-WAIT sockets 重新用于新的TCP 连接
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_fin_timeout = 1
#当keepalive 起用的时候，TCP 发送keepalive 消息的频度。缺省是2 小时
net.ipv4.tcp_keepalive_time = 1800
net.ipv4.tcp_keepalive_probes = 3
net.ipv4.tcp_keepalive_intvl = 15
#允许系统打开的端口范围
#net.ipv4.ip_local_port_range = 1024    65000
#修改防火墙表大小，默认65536
#net.netfilter.nf_conntrack_max=655350
#net.netfilter.nf_conntrack_tcp_timeout_established=1200
# 确保无人能修改路由表
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
net.ipv4.conf.default.secure_redirects = 0
#优化redis启动警告
vm.overcommit_memory = 1
net.core.somaxconn=32768
EOF
echo never > /sys/kernel/mm/transparent_hugepage/enabled
sysctl -p


# After landing display information
echo "It is product environment,be careful..." > /etc/motd

# Ban Ctrl+Alt+Del
mv /usr/lib/systemd/system/ctrl-alt-del.target /usr/lib/systemd/system/ctrl-alt-del.target.bakup
init q

# Add user
# echo "Please enter your user name"
# read user
# useradd $user
# for (( i=0; i <= 3; i++ ))
# do
    # echo "Please enter the password"
    # read password
    # echo "try aging enter the password"
    # read passwordtry
    # if [ $password == $passwordtry ]; then
        # passwd $user $password
    # else
        # echo "Two input password, please try again!"
    # fi
# done
# Lock key file system
#chattr +i /etc/passwd
#chattr +i /etc/inittab
#chattr +i /etc/group
#chattr +i /etc/shadow
#chattr +i /etc/gshadow

#mv /usr/bin/chattr /usr/bin/chattrs

# Remove unwanted users
userdel adm
userdel lp
userdel sync
userdel shutdown
userdel halt
userdel news
userdel uucp
userdel operator
userdel games
userdel gopher
userdel ftp
# Remove unnecessary group
groupdel adm
groupdel lp
groupdel news
groupdel uucp
groupdel games
groupdel dip
groupdel pppusers

#create project deploye files

roots="new_project"
down="download"
git="git"
#shell="shells"

mkdir /home/$roots
mkdir /home/$roots/$down
mkdir /home/$roots/$down/$git
#mkdir /home/$roots/$down/$shells