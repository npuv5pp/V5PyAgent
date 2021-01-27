import socket
import proto.API_pb2
import uuid

class V5receiver:#平台发出请求，adapter接收
    def __init__(self) -> None:
        self.client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.client.bind(('127.0.0.1', xxx))#平台的port
        self.client.settimeout(10)#10stimeout
        self.isDisposed=False
        self.cacheitem=None
        self.breakFlag=False
    
    def Call(self,payload:bytes,retryInterval=50):
        def SendMe():
            self.client.send(outBuffer)

        packet=V5Packet().MakeRequestPacket(payload)
        outBuffer=packet.packet2bytes()
        outGuid=packet.requestId#存放uuid(GUID)
        
        #TODO


class CacheItem:
    def __init__(self) -> None:
        self.requestId=None#UUID
        self.response=None#bytes

class V5poster:#adapter
    def __init__(self,port:int) -> None:
        self.client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.client.bind(("127.0.0.1",port))
        self.isDisposed=False
        self.breakFlag=False
        self.lastResponse=CacheItem()#CacheItem

    def run(self):
        if self.isDisposed is True:
            raise socket.error#Disposed is True
        self.breakFlag=False
        while (not self.isDisposed) and (not self.breakFlag):
            try:
                data,adress=self.client.recvfrom(1024)
                inpacket=V5Packet()
                inpacket.bytes2packet(data)
                response=None

                if self.lastResponse.requestId is inpacket.requestId:#重发
                    response=self.lastResponse.response#bytes
                else:
                    strategy=transfer()
                    response=strategy.ServerRoutine(inpacket.payload)#TODO 获取代码的返回值

                    if response is None:
                        response=bytes()
                    self.lastResponse.requestId=inpacket.requestId
                    self.lastResponse.response=response
                
                outpacket=V5Packet()
                outpacket.MakeResponsePacket(response,inpacket.requestId)
                self.client.sendto(outpacket.packet2bytes(),adress)
            except socket.error:
                print("V5poster遇到socketerror")

class transfer:#protobuf信息->bytes
    def __init__(self) -> None:
        self.call=pyadapter.proto.API_pb2.RPCCall()
    def ServerRoutine(self,protobufmsg):
        self.call.ParseFromString(protobufmsg)
        case=self.call.MethodCase
        print(case)

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
    def MakeResponsePacket(self,payload:bytes,requestId:uuid.UUID):
        if len(payload)>65535:
            raise ValueError#传输过长
        self.magic=self.MAGIC
        self.requestId=requestId
        self.flags=0
        self.length=len(payload)
        self.Reply=True
        return self
    def CheckFlag(self,mask:int):#对应原代码的get
        return (self.flags&mask) is not 0
    def AssignFlag(self,mask:int,x:bool):#对应原代码的set
        if x is True:
            self.flags=self.flags|mask
        else:
            self.flags=self.flags&(0b11111111-mask)#相当于flag 与 (八位取反mask)
    def packet2bytes(self) -> bytes:#TODO 可能UUID(4字节) 端序有问题
        press=self.MAGIC.to_bytes(4,byteorder="little",signed=False)+\
                self.requestId.bytes+\
                self.flags.to_bytes(1,byteorder="little",signed=False)+\
                self.length.to_bytes(2,byteorder="little",signed=False)+\
                self.payload
        return press
    def bytes2packet(self,press:bytes):
        self.magic=int.from_bytes(press[0:4],byteorder="little")
        self.requestId=uuid.UUID(bytes=press[4:20])#没问题了
        self.flags=int.from_bytes(press[20:21],byteorder="little")
        self.length=int.from_bytes(press[21:23],byteorder="little")
        self.payload=press[23:]
        print("payload",self.payload)#DELETE
        return self
