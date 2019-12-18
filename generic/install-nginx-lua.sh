#!/bin/bash
#带lua的nginx脚本

yum install -y wget  gcc  gcc-c++
#基础依赖
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/nginx-1.12.2.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openssl-1.0.2q.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/pcre-8.41.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/zlib-1.2.11.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/perl-5.30.1.tar.gz
#下载lua依赖
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/luajit2-2.1-20190912.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/lua-nginx-module-0.10.15.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/ngx_devel_kit-0.3.1.tar.gz

tar -zxvf luajit2-2.1-20190912.tar.gz
tar -zxvf lua-nginx-module-0.10.15.tar.gz
tar -zxvf ngx_devel_kit-0.3.1.tar.gz
cd luajit2-2.1-20190912
make install
#回退
cd ..

tar -xzf perl-5.30.1.tar.gz
cd perl-5.30.1
./Configure -des -Dprefix=$HOME/localperl
make
make test
make install
cd ..
tar -zxvf nginx-1.12.2.tar.gz
tar -zxvf openssl-1.0.2q.tar.gz
tar -zxvf pcre-8.41.tar.gz
tar -zxvf zlib-1.2.11.tar.gz
cd nginx-1.12.2
export LUAJIT_LIB=/usr/local/lib
export LUAJIT_INC=/usr/local/include/luajit-2.1
./configure --prefix=/usr/local/nginx  --with-ld-opt="-Wl,-rpath,/usr/local/lib"  --add-module=../ngx_devel_kit-0.3.1  --add-module=../lua-nginx-module-0.10.15 --with-pcre=../pcre-8.41 --with-zlib=../zlib-1.2.11 --with-http_ssl_module   --with-openssl=../openssl-1.0.2q
make -j2 && make install
cd /usr/local/nginx/conf
mkdir vhost
rm -rf nginx.conf
wget -c https://raw.githubusercontent.com/1030907690/public-script/master/generic/nginx-lua.conf
mv nginx-lua.conf nginx.conf