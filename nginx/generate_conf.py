# -*- coding: utf-8 -*-

'''
生成https文件
'''
import requests

if __name__ == '__main__':

    network_prefix = "https://raw.githubusercontent.com/1030907690/public-script/master/nginx/conf/"
    conf_list = ["nginx-conf-templa-dynamic-http.conf", "nginx-conf-templa-dynamic-https.conf",
                 "nginx-conf-templa-static-http.conf", "nginx-conf-templa-static-https.conf"]

    random = input("请输入: dynamic-http 0 , dynamic-https 1 , static-http 2 static-https 3 ")

    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get(network_prefix + conf_list[int(random)], headers=headers,timeout=999)
        content = response.text
        port = input("请输入端口")
        content = content.replace("#port#",port)

        domain = input("请输入域名")
        content = content.replace("#domain#",domain)

        domain_suffix = input("证书名称一般是一级域名")
        content = content.replace("#domain_suffix#", domain_suffix)

        proxy_pass = input("请输入代理地址proxy_pass")
        content = content.replace("#proxy_pass#", proxy_pass)

        print(content)
        file_name = domain+port
        with open('%s.conf' % file_name, 'w') as f:  # 设置文件对象
            f.write(content)
    except Exception as e:
        print("program error %s " % e)
    finally:
        print("finally print!")
