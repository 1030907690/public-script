#!/bin/bash
#yum install -y docker
systemctl start docker
mkdir -p /data/gitlab
# 如果有需要可以自己改下 hostname gitlab.example.com,改成自己的,不改也没太多影响
docker run --detach  --hostname gitlab.example.com --publish 444:443 --publish 8881:80 --publish 23:22  --name gitlab-standard   --restart always  --volume /data/gitlab/config:/etc/gitlab   --volume /data/gitlab/logs:/var/log/gitlab   --volume /data/gitlab/data:/var/opt/gitlab  docker.io/gitlab/gitlab-ce
echo "端口对应关系  444:443 8881:80  23:22  14版本开始默认密码在容器内/etc/gitlab/initial_root_password文件中"
