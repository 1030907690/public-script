#!/bin/bash
mkdir ~/.pip
touch ~/.pip/pip.conf
echo "
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com" > ~/.pip/pip.conf
