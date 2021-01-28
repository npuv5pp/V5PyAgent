import random
from typing import Tuple
from v5rpcstruct import *

@catchall
def on_event(eventType: int, args: EventArguments):
    event = {
        0:lambda :print(args.JudgeResult.Reason),
        1:lambda :print("Match Start"),
        2:lambda :print("Match Stop"),
        3:lambda :print("First Half Start"),
        4:lambda :print("Second Half Start"),
        5:lambda :print("Overtime Start"),
        6:lambda :print("Penalty Shootout Start")
    }
    event[eventType]()


@catchall
def get_team_info(serverVersion: int) -> str:
    version = {
        0:"V1.0",
        1:"V1.1"
    }
    print(f'server rpc version: {version.get(serverVersion,"V1.0")}')
    return 'Python Strategy Server'
    

f=None
e=None
@catchall
def get_instruction(field:Field):
    global f
    global e
    field.Postion#这是一个运行时错误
    return [(20, -20), (10, 10), (0, 0), (0, 0), (0, 0)],0
    if(field.SelfRobots[0].Rotation<-179 or field.SelfRobots[0].Rotation>179):
        return [(125, 125), (0, 0), (0, 0), (0, 0), (0, 0)],0
    else:
        return [(20, -20), (0, 0), (0, 0), (0, 0), (0, 0)],0


@catchall
def get_placement(field: Field) -> List[Tuple[float, float, float]]:
    # pos=[]
    # pos.append((0,10,0))
    # for i in range(1,6):
    #     pos.append((50,50-i*10,0))
    # return pos
    return [(0, 0, 0),(90, -17, 50),(80, 46, 60),(31, 30, 0),(-11, 50, 0),(0, 0, 0)]#最后一个是球位置
    #return [(random.randint(-50, 50), random.randint(-50, 50), 0) for _ in range(6)]

def initial(field: Field) -> Field:
    return Field(field)

