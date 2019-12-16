#!/bin/bash

#卸载openjdk
openjdks=`rpm -qa | grep openjdk`
for i in $openjdks;
do
  echo "yum -y remove " $i
  yum -y remove $i
done

yum install -y wget gcc gcc-c++
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/jdk8/jdk-8u144-linux-x64.tar.gz
tar -zxvf jdk-8u144-linux-x64.tar.gz
cp -R jdk1.8.0_144 /usr/local/
echo 'export JAVA_HOME=/usr/local/jdk1.8.0_144' >> /etc/profile
echo 'export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar' >> /etc/profile
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
source /etc/profile