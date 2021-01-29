import sys
import os
import V5RPC

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

args = sys.argv
# 0参数：start.py
# 1参数: 端口
port = int(args[1])

server = V5RPC.V5Poster(port)
server.run()
