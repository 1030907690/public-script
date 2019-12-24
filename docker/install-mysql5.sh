#!/bin/bash
#安装mysql5.7
yum install -y docker
systemctl start docker
docker run -p 3306:3306 --name mysql5.7_3306 -v /etc/localtime:/etc/localtime:ro   -e MYSQL_ROOT_PASSWORD=root -d docker.io/mysql:5.7