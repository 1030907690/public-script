 local _M = {}
cache_str = nil;
function _M.run()
    ngx.req.read_body()
    local post_args = ngx.req.get_post_args()
   
    -- local cmd = post_args["cmd"]
    if nil == cache_str then
		local cmd = '/usr/local/openresty/nginx/html/index3.html'
		f_ret,err = io.open(cmd)
		-- ngx.say(err)
		-- ngx.say( ngx.null)
		
		if nil == err then
			local ret = f_ret:read("*a")
			cache_str = ret
			-- ngx.say('ret'.. ret .. 'res')
			--ngx.say("save cache")
		end
	end
	--ngx.say('cache_str: '.. cache_str)
	ngx.say(cache_str)
	-- 获取header
	--local headers = ngx.req.get_headers()
	--for k,v in pairs(headers) do
	--	ngx.say("[header] name: " ,k," v: ",v .."</br>")
	--end
	
	--ngx.say("</br>")
	-- 获取get请求参数
	-- local arg 
end	
return _M