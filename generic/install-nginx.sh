#!/bin/bash
yum install -y wget  gcc  gcc-c++
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/nginx-1.12.2.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openssl-1.0.2q.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/pcre-8.41.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/zlib-1.2.11.tar.gz
wget -c https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/perl-5.30.1.tar.gz
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
./configure --prefix=/usr/local/nginx  --with-pcre=../pcre-8.41 --with-zlib=../zlib-1.2.11 --with-http_ssl_module   --with-openssl=../openssl-1.0.2q --with-http_gunzip_module
make && make install