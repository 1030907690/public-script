#!/bin/bash
#sh auto-restart.sh > logs.log 2>&1 &
my_array=(":download-1.0.0-SNAPSHOT.jar" ":dmdownload-1.0.0-SNAPSHOT.jar")
work_space_array=("/home/new_project/download/" "/home/new_project/dmdownload/")

length=${#my_array[@]}
while true
do
        echo "scanning......" `date +"%Y-%m-%d %H:%M:%S"`
        #for i in ${my_array[*]} ;
        for ((i=0; i<$length; i++))
        do
           proId=`ps -ef | grep ${my_array[$i]} |grep -v 'grep' | awk '{print $2}'`
           if [ x"$proId" = x ]; then
               echo ${my_array[$i]} " abnormal "
               echo "restart "${my_array[$i]} "chdir" ${work_space_array[$i]}
               cd ${work_space_array[$i]}
               sh start.sh
			         sleep 20s
               pro_id_item=`ps -ef | grep ${my_array[$i]} |grep -v 'grep' | awk '{print $2}'`
               if [ x"$pro_id_item" = x ]; then
                  echo ${my_array[$i]}" restart fail "
                else
                  echo ${my_array[$i]}" restart successful pid " $pro_id_item
                fi
            else
              echo ${my_array[$i]} " normal " $proId
            fi
        done
        sleep 1m
done