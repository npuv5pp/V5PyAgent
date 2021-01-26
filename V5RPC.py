from enum import Flag
import socket
import uuid

class V5receiver:#平台发出请求，adapter接收
    def __init__(self) -> None:
        self.client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.client.bind(('127.0.0.1', 20000))
        self.client.settimeout(10)#10stimeout
        self.isDisposed=False
        self.cacheitem=None
        self.breakFlag=False
    
    def Call(self,payload:bytes,retryInterval=50):
        packet=V5Packet().MakeRequestPacket(payload)
        outBuffer=bytes()
        outGuid=packet.requestId#存放uuid(GUID)
        
        #TODO

class V5poster:#adapter传出信息
    def __init__(self) -> None:
        pass
        

class V5Packet:#通信协议
    MAGIC=0x2b2b3556
    REPLY_MASK=0x1
    def __init__(self) -> None:
        self.magic=None#uint
        self.requestId=None#GUID
        self.flags=None#byte
        self.length=None#ushort
        self.payload=bytes()#bytes
    def MakeRequestPacket(self,payload:bytes):
        if len(payload)>65535:
            raise ValueError#传输过长
        self.magic=self.MAGIC
        self.requestId=uuid.uuid1()
        self.flags=0
        self.length=len(payload)
        self.payload=payload
        self.Reply = False
        return self
    def CheckFlag(self,mask:int):#对应原代码的get
        return (self.flags&mask) is not 0
    def AssignFlag(self,mask:int,x:bool):#对应原代码的set
        if x is True:
            self.flags=self.flags|mask
        else:
            self.flags=self.flags&(0b11111111-mask)#相当于flag 与 (八位取反mask)
