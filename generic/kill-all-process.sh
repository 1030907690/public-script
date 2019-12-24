#!/bin/bash
proIds=`ps -ef | grep $1 |grep -v 'grep' | awk '{print $2}'`
for i in $proIds;
do
  echo "kill -15 " $i
  kill -15 $i
done