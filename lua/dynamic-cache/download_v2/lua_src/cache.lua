


-- 缓存文件
 local _M = {}
-- cache_tab = {}
function _M.cache()

	local promotion_cache = ngx.shared.promotion_cache
	local httpUri = ngx.var.request_uri
	 
	-- 刷新缓存uri
	local refresh = "/test/refresh.html"
	if refresh == httpUri then
        -- 缓存清空
		--cache_tab = {}
		promotion_cache:flush_all()
		promotion_cache:flush_expired(10)
						
		ngx.say("cache refresh successful")
	else  -- html的请求
		
		local body_html = promotion_cache:get(httpUri)
		-- if nil == cache_tab[httpUri] then
		   if nil == body_html then
			-- 没有这个的缓存数据 ，尝试请求
				-- ngx.say(httpUri)
				-- 发起子请求
				local res = ngx.location.capture(httpUri.."s")
				ngx.say(res.body)
				-- 保存缓存
				-- cache_tab[httpUri] = res.body
				promotion_cache:set(httpUri,res.body)
				-- ngx.say("not found")
				 
		else
			-- ngx.say("found")
			-- 有这个缓存
			-- ngx.say(cache_tab[httpUri])
			ngx.say(body_html)
		end
	end
	
	-- ngx.say("test")

end
return _M


 