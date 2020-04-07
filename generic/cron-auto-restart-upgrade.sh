#!/bin/bash
#*/5 * * * *   sh /root/software/cron-auto-restart-upgrade.sh
export JAVA_HOME=/usr/local/jdk1.8.0_144 
export JRE_HOME=$JAVA_HOME/jre
export PATH=$PATH:$JAVA_HOME/bin
my_array=("https://toz66.app")
pro_array=(":dmdownload-1.0.0-SNAPSHOT.jar")
work_space_array=("/home/new_project/dmdownload/")

length=${#my_array[@]}
echo "scanning......" `date +"%Y-%m-%d %H:%M:%S"`
#for i in ${my_array[*]} ;
for ((i=0; i<$length; i++))
do
  proId=`curl -I -m 10 -o /dev/null -s -w %{http_code}  ${my_array[$i]}`;
  if [ "$proId"x != "200"x ]; then
      #try kill process
      kill_pro_id=`ps -ef | grep ${pro_array[$i]} |grep -v 'grep' | awk '{print $2}'`
      kill -15 $kill_pro_id
      sleep 5s
	    echo ${my_array[$i]} " abnormal "
	    echo "restart "${my_array[$i]} "chdir" ${work_space_array[$i]}
	    cd ${work_space_array[$i]}
	    sh start.sh

	  sleep 30s
    #try find process
    pro_id_item=`ps -ef | grep ${pro_array[$i]} |grep -v 'grep' | awk '{print $2}'`

	  if [ x"$pro_id_item" = x ]; then
		  echo ${my_array[$i]}" restart fail "
		else
		  echo ${my_array[$i]}" restart successful pid " $pro_id_item
		fi
	else
	  echo ${my_array[$i]} " normal " $proId
	fi
done