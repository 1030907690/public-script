#!/bin/bash
#redis5.0.7 密码root
yum install -y docker wget
systemctl start docker
mkdir -p /data/redis/conf
cd /data/redis/conf
wget -c https://raw.githubusercontent.com/1030907690/public-script/master/docker/redis.conf
docker run  --privileged=true -d -p 6379:6379 -v /data/redis/conf:/usr/local/etc/redis --name redis-standard redis:5.0.7 redis-server /usr/local/etc/redis/redis.conf
echo "redis密码root"