
local _M = {}
function _M.short_url()
 local args = ngx.req.get_uri_args()
 local http_uri = ngx.var.request_uri
 local short_url_uri = "/short.do"

 if  nil ~= string.find(http_uri,short_url_uri) then
	
		ngx.header.content_type = 'text/json'
		local functions = require('short/functions')
		-- local cjson = require('cjson')
		local args = ngx.req.get_uri_args()

		local long_url = args['url']
		local short_string = args['short']
		--ngx.say("url   "..long_url)
		local short_url_val, err = functions.url_create(long_url)
		if err then
			functions.show_error(err)
		end
		ngx.say('{"status":1,"shorturl":"'..short_url_val..'"}')	
 
 else
	--ngx.say("重定向")
	ngx.header.content_type = 'text/html'
	local config = require('short/config')
	local functions = require('short/functions')
	local short_string = string.sub(ngx.var.uri, -#config['start_url'])
	 
	local long_url, err = functions.get_long_url(short_string)
	if err then
		functions.show_error(err)
	end
	ngx.redirect(long_url)
 end
 
 
end
return _M