import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import V5RPC

args = sys.argv
# 0参数：start.py
# 1参数: 端口
port = int(args[1])

server = V5RPC.V5Poster(port)
server.run()
