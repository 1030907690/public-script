#!/bin/bash
if [ `grep -c "Ubuntu"  /etc/issue` -eq '0' ]; then
    echo "当前系统是其他系统!"
yum install -y wget  gcc  gcc-c++ g++
#基础依赖
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openssl-1.0.2q.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/pcre-8.41.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/zlib-1.2.11.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/perl-5.30.1.tar.gz

#nginx 打印
#wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/echo-nginx-module-0.61.tar.gz



tar -zxvf perl-5.30.1.tar.gz
cd perl-5.30.1
./Configure -des -Dprefix=$HOME/localperl
make
make test
make install
cd ..
#tar -zxvf echo-nginx-module-0.61.tar.gz
tar -zxvf openresty-1.15.8.2.tar.gz
tar -zxvf openssl-1.0.2q.tar.gz
tar -zxvf pcre-8.41.tar.gz
tar -zxvf zlib-1.2.11.tar.gz

cd openresty-1.15.8.2
#--add-module=../echo-nginx-module-0.61
./configure --prefix=/usr/local/openresty --with-pcre=../pcre-8.41 --with-zlib=../zlib-1.2.11 --with-http_ssl_module   --with-openssl=../openssl-1.0.2q
make && make install
cd /usr/local/openresty
mkdir nginx/conf/vhost
#追加字符串
sed -i 'N;116 a include vhost/*.conf;' nginx/conf/nginx.conf
ln -s /usr/local/openresty/bin/openresty /usr/bin/openresty

else
  echo "当前系统是其他系统Ubuntu"
  apt-get install -y wget gcc gcc-c++
   #基础依赖
  wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz
  wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openssl-1.0.2q.tar.gz
  wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/pcre-8.41.tar.gz
  wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/zlib-1.2.11.tar.gz
  wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/perl-5.30.1.tar.gz

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
fi