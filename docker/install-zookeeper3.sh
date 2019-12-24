#!/bin/bash
#安装zookeeper3.4
yum install -y docker wget
systemctl start docker
mkdir -p /data/zookeeper/conf
cd /data/zookeeper/conf
wget -c https://raw.githubusercontent.com/1030907690/public-script/master/docker/zoo.cfg
docker pull zookeeper:3.4
docker run --privileged=true -p 2181:2181 --name  zookeeper-standard --restart always -d -v /data/zookeeper/conf/zoo.cfg:/conf/zoo.cfg zookeeper:3.4