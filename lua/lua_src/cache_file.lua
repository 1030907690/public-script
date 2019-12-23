-- 缓存文件
 local _M = {}
cache_tab = {};
function _M.cache()
     local existence = false
    -- 静态文件前缀
    local prefix = "/usr/local/openresty/nginx/html"
    local httpUri = ngx.var.request_uri
    if nil == cache_tab[httpUri] then
	
	    local file = io.open(prefix..httpUri, "rb")
		if file then
			local ret = file:read("*a")
            if nil ~= ret then
				cache_tab[httpUri] = ret
				existence = true
				-- ngx.say("save cache")
			end
			file:close()
		else
		    existence = false
           -- ngx.say("404 Not Found")
		end
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
return _M