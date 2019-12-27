

-- 代理的第一个方法 修改值
-- ngx.var.new_uri = "192.168.137.137:81/index.html"

--代理的第二个办法 子请求
res = ngx.location.capture("/proxypasstest/index2.html")
ngx.say(res.body)
