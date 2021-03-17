import sys
import os
from adapter.v5rpc import V5RPC

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

if len(sys.argv) >= 2:
    listen_port = int(sys.argv[1])
else:
    listen_port = 20000

server = V5RPC.V5Poster(listen_port)
server.run()
