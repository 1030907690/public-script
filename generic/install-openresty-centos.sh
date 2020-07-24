#!/bin/bash
yum install -y wget  gcc  gcc-c++ g++
#基础依赖
wget -O openresty-1.15.8.2.tar.gz -c https://sourceforge.net/projects/generic-software/files/php/openresty-1.15.8.2.tar.gz
wget -O openssl-1.0.2q.tar.gz -c https://sourceforge.net/projects/generic-software/files/php/openssl-1.0.2q.tar.gz
wget -O pcre-8.41.tar.gz -c https://sourceforge.net/projects/generic-software/files/php/pcre-8.41.tar.gz
wget -O zlib-1.2.11.tar.gz -c https://sourceforge.net/projects/generic-software/files/php/zlib-1.2.11.tar.gz
wget -O perl-5.30.1.tar.gz -c https://sourceforge.net/projects/generic-software/files/php/perl-5.30.1.tar.gz


tar -zxvf perl-5.30.1.tar.gz
cd perl-5.30.1
./Configure -des -Dprefix=$HOME/localperl
make
make test
make install
cd ..
tar -zxvf openresty-1.15.8.2.tar.gz
tar -zxvf openssl-1.0.2q.tar.gz
tar -zxvf pcre-8.41.tar.gz
tar -zxvf zlib-1.2.11.tar.gz

cd openresty-1.15.8.2
./configure --prefix=/usr/local/openresty --with-pcre=../pcre-8.41 --with-zlib=../zlib-1.2.11 --with-http_ssl_module   --with-openssl=../openssl-1.0.2q
make && make install
cd /usr/local/openresty
mkdir nginx/conf/vhost
#追加字符串
sed -i 'N;116 a include vhost/*.conf;' nginx/conf/nginx.conf
ln -s /usr/local/openresty/bin/openresty /usr/bin/openresty
echo "安装完成，可以使用openresty启动试试"