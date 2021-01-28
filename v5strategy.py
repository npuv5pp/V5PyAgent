import random
from typing import Tuple
from v5rpcstruct import *


def on_event(eventType: int, args: EventArguments):
    event = {
        0:lambda :print(args.judge_result.reason),
        1:lambda :print("Match Start"),
        2:lambda :print("Match Stop"),
        3:lambda :print("First Half Start"),
        4:lambda :print("Second Half Start"),
        5:lambda :print("Overtime Start"),
        6:lambda :print("Penalty Shootout Start")
    }
    event[eventType]()



def get_team_info(serverVersion: int) -> str:
    version = {
        0:"V1.0",
        1:"V1.1"
    }
    print(f'server rpc version: {version.get(serverVersion,"V1.0")}')
    return 'Python Strategy Server'
    

f=None
e=None

def get_instruction(field:Field):
    global f
    global e
    print(field.tick)
    return [(20, -20), (10, 10), (0, 0), (0, 0), (0, 0)],0



def get_placement(field: Field) -> List[Tuple[float, float, float]]:
    # pos=[]
    # pos.append((0,10,0))
    # for i in range(1,6):
    #     pos.append((50,50-i*10,0))
    # return pos
    return [(42,42, 180),(42, 42, 180),(42, 42, 180),(42, 42, 180),(42, 42, 180),(0.0, 0.0, 0.0)]#最后一个是球位置
    #return [(random.randint(-50, 50), random.randint(-50, 50), 0) for _ in range(6)]

