import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import V5RPC

port = 20000

server = V5RPC.V5Poster(port)
server.run()
