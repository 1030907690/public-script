#!/bin/bash
#yum install -y docker
systemctl start docker
mkdir -p /data/gitlab
docker run --detach  --hostname gitlab.example.com --publish 443:443 --publish 8881:80 --publish 23:22  --name gitlab-standard   --restart always  --volume /data/gitlab/config:/etc/gitlab   --volume /data/gitlab/logs:/var/log/gitlab   --volume /data/gitlab/data:/var/opt/gitlab  docker.io/gitlab/gitlab-ce
echo "端口对应关系  443:443 8881:80  23:22 "