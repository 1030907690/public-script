#!/bin/bash
yum install -y wget  gcc  gcc-c++
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/redis/redis.conf
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/redis/redis-5.0.6.tar.gz
tar -zxvf redis-5.0.6.tar.gz
cd redis-5.0.6
make MALLOC=libc
cd src
./redis-server ../../redis.conf
echo '密码为root'
