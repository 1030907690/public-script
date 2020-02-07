#!/bin/bash
path="$1"
read_dir(){
    for file in `ls $path`       #注意此处这是两个反引号，表示运行系统命令
    do
        if [ -d $path"/"$file ]  #注意此处之间一定要加上空格，否则会报错
        then
            #read_dir $path"/"$file
            echo "文件夹 " $path"/"$file
            cd $path"/"$file
            git pull
        else
           #echo $path"/"$file   #在此处处理文件即可
           echo ''
        fi
    done
}
#读取第一个参数
if [ "$path"x = "."x ];
then
 path=`pwd`
fi
read_dir $path