#!/bin/bash
#安装Python3.5.2脚本
if [ `grep -c "Ubuntu"  /etc/issue` -eq '0' ]; then
    echo "当前系统是其他系统!"
    yum install -y wget
    yum install -y gcc gcc-c++
    yum install -y openssl-devel
    wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/python/sqlite-autoconf-3300100.tar.gz
    tar -zxvf sqlite-autoconf-3300100.tar.gz
    cd sqlite-autoconf-3300100
    ./configure --prefix=/usr/local/sqlite3
    make && make install
    #回退
    cd ..
    wget -c https://excellmedia.dl.sourceforge.net/project/generic-software/python/Python-3.5.2.tgz
    tar -zxvf Python-3.5.2.tgz
    cd Python-3.5.2
    ./configure --prefix=/usr/local/python3.5
    echo "如果要增加sqlite3模块请先在setup.py sqlite_inc_paths数组中增加 '/usr/local/sqlite3/include', "
    read -p "Enter Continue:" name
    make && make install
    ln -s /usr/local/python3.5/bin/python3.5 /usr/bin/python3.5
    ln -s /usr/local/python3.5/bin/pip3.5 /usr/bin/pip3.5
else
    echo "当前系统是其他系统Ubuntu"
    apt-get install -y wget
    apt-get install -y gcc
    apt-get install -y libssl-dev
    apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
    apt-get install -y libssl1.0

    wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/python/sqlite-autoconf-3300100.tar.gz
    tar -zxvf sqlite-autoconf-3300100.tar.gz
    cd sqlite-autoconf-3300100
    ./configure --prefix=/usr/local/sqlite3
    make && make install
    #回退
    cd ..

    wget -c https://excellmedia.dl.sourceforge.net/project/generic-software/python/Python-3.5.2.tgz
    tar -zxvf Python-3.5.2.tgz
    cd Python-3.5.2
    ./configure --prefix=/usr/local/python3.5  --enable-shared
    echo "如果要增加sqlite3模块请先在setup.py sqlite_inc_paths数组中增加 '/usr/local/sqlite3/include', "
    read -p "Enter Continue:" name
    make && make install
    ln -s /usr/local/python3.5/bin/python3.5 /usr/bin/python3.5
    ln -s /usr/local/python3.5/bin/pip3.5 /usr/bin/pip3.5
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/python3.5/lib' >> /etc/profile
fi

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/python3.5/lib' >> /etc/profile
echo '请使用命令 source /etc/profile 重载对$LD_LIBRARY_PATH变量的新增 '