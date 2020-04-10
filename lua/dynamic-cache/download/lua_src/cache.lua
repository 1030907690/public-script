


-- 缓存文件
 local _M = {}
cache_tab = {}
function _M.cache()

	local httpUri = ngx.var.request_uri
	 
	-- 刷新缓存uri
	local refresh = "/test/refresh.html"
	if refresh == httpUri then
        -- 缓存清空
		cache_tab = {}
		ngx.say("cache refresh successful")
	else  -- html的请求
		if nil == cache_tab[httpUri] then
			-- 没有这个的缓存数据 ，尝试请求
				ngx.say(httpUri)
				-- 发起子请求
				res = ngx.location.capture(httpUri.."s")
				ngx.say(res.body)
				-- 保存缓存
				cache_tab[httpUri] = res.body
				-- ngx.say("not found")
				 
		else
			-- ngx.say("found")
			-- 有这个缓存
			ngx.say(cache_tab[httpUri])
		end
	end
	
	-- ngx.say("test")

end
return _M


 