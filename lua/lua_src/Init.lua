local p = "/usr/local/openresty/nginx/conf/lua_src/"
local m_package_path = package.path
package.path = string.format("%s?.lua;%s?/init.lua;%s", p, p, m_package_path)
cmd = require("t")
cache = require("cache_file")
short_cmd = require("short_url")