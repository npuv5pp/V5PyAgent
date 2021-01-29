import random
from typing import Tuple
from v5rpc import *


def on_event(eventType: int, args: EventArguments):
    event = {
        0: lambda: print(args.judge_result.reason),
        1: lambda: print("Match Start"),
        2: lambda: print("Match Stop"),
        3: lambda: print("First Half Start"),
        4: lambda: print("Second Half Start"),
        5: lambda: print("Overtime Start"),
        6: lambda: print("Penalty Shootout Start")
    }
    event[eventType]()


def get_team_info(serverVersion: int) -> str:
    version = {
        0: "V1.0",
        1: "V1.1"
    }
    print(f'server rpc version: {version.get(serverVersion, "V1.0")}')
    return 'Python Strategy Server'


def get_instruction(field: Field):
    print(field.tick)  # tick从2起始
    if field.tick % 60 != 0:
        return [(20, -20), (10, 10), (0, 0), (0, 0), (0, 0)], 0
    else:
        return [(20, -20), (10, 10), (0, 0), (0, 0), (0, 0)], 1  # 以第二元素的(0,1)表明重置开关,1表示重置


def get_placement(field: Field) -> List[Tuple[float, float, float]]:
    return [(42, 42, 180), (42, 42, 180), (42, 42, 180), (42, 42, 180), (42, 42, 180),
            (0.0, 0.0, 0.0)]  # 最后一个是球位置（x,y,角）,角其实没用
