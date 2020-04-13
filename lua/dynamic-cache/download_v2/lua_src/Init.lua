local p = "D:/software/openresty-1.15.8.3-win64/conf/lua_src/"
local m_package_path = package.path
package.path = string.format("%s?.lua;%s?/init.lua;%s", p, p, m_package_path)
cache = require("cache")
 