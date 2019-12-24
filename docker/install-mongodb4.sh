#!/bin/bash
yum install -y docker
systemctl start docker
mkdir -p /data/mongodb/datadir
docker run -p 27017:27017 --privileged=true -d --name mongo-standard  -v /data/mongodb/datadir:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo:4.0
echo "mongodb账户密码都是密码root"
echo "登录进入容器可以用命令 mongo --port 27017 -u "root" -p "root" --authenticationDatabase \"admin\" 连接"