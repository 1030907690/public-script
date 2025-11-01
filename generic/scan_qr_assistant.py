'''
扫码助手
Zhou Zhongqing
2025-10-29 21:30:00
'''

# 导入必要的模块
import socket
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

#  参考 https://segmentfault.com/a/1190000044701510
# 定义一个简单的HTTP服务器类
class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        try:
            # 创建一个TCP套接字
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置套接字选项，允许地址重用
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 绑定主机和端口
            self.server_socket.bind((self.host, self.port))
            # 监听连接
            self.server_socket.listen(5)
            print("HTTP 服务器已启动，监听地址：%s，端口：%d" % (self.host, self.port))

            while True:
                # 接受连接
                client_socket, client_address = self.server_socket.accept()
                print("接收到来自 %s 的连接" % str(client_address))
                # 处理HTTP请求
                self.handle_request(client_socket)

        except Exception as e:
            print("`发生异常：%s" % str(e))

        finally:
            if self.server_socket:
                self.server_socket.close()
                print("HTTP 服务器已关闭")

    def handle_request(self, client_socket):
        # 接收客户端请求数据
        request_data = client_socket.recv(1024).decode('utf-8')
        # 解析请求
        request_lines = request_data.split('\n')
        if request_lines:
            # 获取请求方法、路径和HTTP版本
            method, path, http_version = request_lines[0].strip().split()
            # print("请求方法：%s，路径：%s，HTTP版本：%s" % (method, path, http_version))
            response_body = ""
            if path.find('/mock_input') >= 0:
                parameter = resolve_parameter(path)
                handler_mock_input(parameter)
                # 构造HTTP响应
                response_body = response_body_format()

            response_headers = [
                "HTTP/1.1 200 OK",
                "Content-Type: text/html",
                "Content-Length: %d" % len(response_body),
                "\n"
            ]
            response = '\n'.join(response_headers) + response_body

            # 发送响应数据到客户端
            client_socket.sendall(response.encode('utf-8'))
            # 关闭客户端连接
            client_socket.close()
            # print("响应已发送")


def handler_mock_input(parameter:dict[str,str]) -> None:
    sn = parameter['sn']
    digest = parameter['digest']
    timestamp = parameter['timestamp']
    # print("sn: %s, digest: %s, timestamp: %s" % (sn , digest, timestamp))
    pynput_input(sn)



def resolve_parameter(path: str) -> dict[str, str]:
    parameter = path.split('?')[1]
    # print("参数：%s" % parameter)

    params = parameter.split("&")
    dict_param:dict[str,str] = {}
    for param in params:
        param_array = param.split('=')
        dict_param[param_array[0]] = param_array[1]
        # print("参数名：%s，参数值：%" % (param.split('=')[0], param.split('=')[1]))
    return dict_param


def response_body_format():
    return '{"code":200,"data":"ok"}'



def pynput_input(str: str):

    str_array: [str] = list(str)
    for key in str_array:
        keyboard.press(key)
        time.sleep(0.001)

    keyboard.press(Key.enter)
# 主函数
if __name__ == "__main__":
    # 服务器主机和端口
    HOST = '0.0.0.0'
    PORT = 8848
    # 创建HTTP服务器实例并启动
    http_server = SimpleHTTPServer(HOST, PORT)
    http_server.start()


#