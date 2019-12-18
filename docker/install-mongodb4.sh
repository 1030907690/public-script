#!/bin/bash
yum install -y docker
systemctl start docker
mkdir -p /data/mongodb/datadir
docker run -p 27017:27017 --privileged=true -d --name mongo-standard  -v /data/mongodb/datadir:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo:4.0
echo "mongodb密码root"