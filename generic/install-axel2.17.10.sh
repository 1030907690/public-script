#!/bin/bash
wget -c https://github.com/axel-download-accelerator/axel/releases/download/v2.17.10/axel-2.17.10.tar.gz
tar -zxvf axel-2.17.10.tar.gz
cd axel-2.17.10
./configure && make && make install

