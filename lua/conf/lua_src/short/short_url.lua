
local _M = {}
function _M.short_url()
 local args = ngx.req.get_uri_args()
 local http_uri = ngx.var.request_uri
 local short_url_uri = "/short.do"
 local root_uri = "/"

 if  nil ~= string.find(http_uri,short_url_uri) then
	
		ngx.header.content_type = 'text/json'
		local functions = require('short/functions')
		-- local cjson = require('cjson')
		-- local args = ngx.req.get_uri_args()

		local long_url = args['url']
		local short_string = args['short']
		--ngx.say("url   "..long_url)
		local short_url_val, err = functions.url_create(long_url)
		if err then
			functions.show_error(err)
		end
		ngx.say('{"status":1,"short_url":"'..short_url_val..'"}')	
 
 elseif root_uri == http_uri then
	ngx.header.content_type = 'text/html'
	local error_html = "<html> <body> <center> <img src=\"https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&amp;quality=100&amp;size=b4000_4000&amp;sec=1577355764&amp;di=0fa924810ceba83a0835e8b4c7f15a58&amp;src=http://n.sinaimg.cn/sinacn17/267/w560h507/20180716/855e-hfkffak7000432.jpg\"></center> </body> </html>"
	ngx.say(error_html)
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