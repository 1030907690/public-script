# public-script
public-script公开的脚本

### Linux解决编写脚本出现"%0D"

    --2020-01-10 11:12:18--  https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz%0D
    正在解析主机 liquidtelecom.dl.sourceforge.net (liquidtelecom.dl.sourceforge.net)... 197.155.77.8
    正在连接 liquidtelecom.dl.sourceforge.net (liquidtelecom.dl.sourceforge.net)|197.155.77.8|:443... 已连接。
    已发出 HTTP 请求，正在等待回应... 302 Moved Temporarily
    位置：https://downloads.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz%0D?download&failedmirror=liquidtelecom.dl.sourceforge.net [跟随至新的 URL]
    --2020-01-10 11:12:19--  https://downloads.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz%0D?download&failedmirror=liquidtelecom.dl.sourceforge.net
    正在解析主机 downloads.sourceforge.net (downloads.sourceforge.net)... 216.105.38.13
    正在连接 downloads.sourceforge.net (downloads.sourceforge.net)|216.105.38.13|:443... 已连接。
    已发出 HTTP 请求，正在等待回应... 404 Not Found


    发现了windwos下,文本文件换行符为CRLF而Linxu下换行符为LF,而在linxu编写的脚本上传到linux就会出现这个问题,所以需要先进行转化一下,需要安装dos2unix

- yum install -y dos2unix
- dos2unix openresty.sh