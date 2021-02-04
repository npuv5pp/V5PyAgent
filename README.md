# PyAdapter
在新平台上加载python strategy

## 文件组成
### 1级目录:

v5rpc.py: 关于平台传送数据的结构的定义，仅是为了方便v5strategy.py调用，无实际效果。即便修改了它，发送数据包的名称仍然不会变。

v5strategy: 四个函数由adapter调用。

>on_event接收比赛状态变化的信息。

>get_team_info控制队名。

>get_instruction控制5个机器人的轮速(leftspeed,rightspeed)，以及最后的reset(1即表明需要reset)

>get_placement控制5个机器人及球在需要摆位时的位置，定位球类的摆位需要符合规则，否则会被重摆

adapter文件夹：

二级目录：

V5RPC.py：adapter核心部分，调用v5strategy，发送数据给平台。

start.py：运行V5RPC.py，port变量可修改端口。

proto文件夹：

三级目录：

三个pb2.py，为protobuf数据包生成的python文件。

.proto：

四级目录：

三个proto文件，定义了protobuf数据包。

##使用

开启start.py即可，pycharm也可用其调试。

win下也可使用.bat调用.pys