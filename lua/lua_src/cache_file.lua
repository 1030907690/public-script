-- 缓存文件
cache_tab = {};
function _M.cache()
    local existence = false
    -- 静态文件前缀
    local prefix = "/usr/local/openresty/nginx/html"
    local httpUri = ngx.var.request_uri
    if nil == cache_tab[httpUri] then
        local f_ret,err = io.open(prefix..httpUri)
        if nil == err then
            local ret = f_ret:read("*a")
            cache_tab[httpUri] = ret
            existence = true
        else
            existence = false
           -- ngx.say("404 Not Found")
        end
         f_ret:close()
    else
        existence = true
    end

    -- 打印结果
    if existence then
        ngx.say(cache_tab[httpUri])
    else
        ngx.say("404 Not Found")
    end

end