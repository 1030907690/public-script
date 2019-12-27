#!/bin/bash
#yum install -y docker
yum install -y yum-utils   device-mapper-persistent-data   lvm2
yum-config-manager  --add-repo   https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --enable docker-ce-edge
yum-config-manager --enable docker-ce-test
yum install -y docker-ce
systemctl start docker