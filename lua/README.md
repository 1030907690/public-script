# lua脚本
> http {
  include       mime.types;
  # lua 文件的位置
  lua_package_path "/usr/local/openresty/nginx/conf/lua_src/?.lua;;";
  # nginx启动阶段时执行的脚本，可以不加
  init_by_lua_file 'conf/lua_src/Init.lua';