

import sys
import v5strategy
import V5RPC

args=sys.argv
#0参数：start.py
#1参数: 端口
port=int(args[1])

server=V5RPC.V5poster(port)
server.run()



