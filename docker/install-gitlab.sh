#!/bin/bash
#yum install -y docker
yum install -y yum-utils   device-mapper-persistent-data   lvm2
yum-config-manager  --add-repo   https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --enable docker-ce-edge
yum-config-manager --enable docker-ce-test
yum install -y docker-ce
systemctl start docker
mkdir -p /data/gitlab
docker run --detach  --hostname gitlab.example.com --publish 443:443 --publish 8881:80 --publish 23:22  --name gitlab   --restart always  --volume /data/gitlab/config:/etc/gitlab   --volume /data/gitlab/logs:/var/log/gitlab   --volume /data/gitlab/data:/var/opt/gitlab  docker.io/gitlab/gitlab-ce
echo "端口对应关系  443:443 8881:80  23:22 "