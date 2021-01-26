import socket

class V5receiver:#平台发出请求，adapter接收
    def __init__(self) -> None:
        self.client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.client.bind(('127.0.0.1', 20000))
        self.isDisposed=False
        self.cacheitem=None
        self.breakFlag=False
        
        
class V5Packet:#transfer，protobuf信息->
    def __init__(self) -> None:
        pass