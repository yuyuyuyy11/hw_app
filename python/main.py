
import sys
import random
import time

n = 200
robot_num = 10
berth_num = 10
boat_num = 5
N = 210
class Robot:
    def __init__(self, startX=0, startY=0, goods=0, status=0, mbx=0, mby=0):
        self.x = startX
        self.y = startY
        self.goods = goods
        self.status = status
        self.mbx = mbx
        self.mby = mby

robot = [Robot() for _ in range(robot_num + 10)]

class Berth:
    def __init__(self, x=0, y=0, transport_time=0, loading_speed=0):
        self.x = x
        self.y = y
        self.transport_time = transport_time
        self.loading_speed = loading_speed

berth = [Berth() for _ in range(berth_num + 10)]

class Boat:
    def __init__(self, num=0, pos=0, status=0):
        self.num = num
        self.pos = pos
        self.status = status

boat = [Boat() for _ in range(10)]


money = 0
boat_capacity = 0
id = 0
ch = []
gds = [[0 for _ in range(N)] for _ in range(N)]

def Init():
    for i in range(0, n):  # 获取200x200地图
        line = input()
        ch.append([c for c in line.split()])
    for i in range(berth_num):  # 获取泊位数据
        line = input()
        berth_list = [int(c) for c in line.split()]
        id = berth_list[0]
        berth[id].x = berth_list[1]
        berth[id].y = berth_list[2]
        berth[id].transport_time = berth_list[3]
        berth[id].loading_speed = berth_list[4]
    boat_capacity = int(input())  # 获取船的容积
    okk = input()
    print("OK")
    sys.stdout.flush()
    
def Input():
    id, money = map(int, input().split())  # 帧序号，当前金币数
    num = int(input())  # 新增货物的数量
    for i in range(num):  # num行新增货物的数量
        x, y, val = map(int, input().split())  # 货物坐标，金额
        gds[x][y] = val
    for i in range(robot_num):  # 10行机器人的信息
        robot[i].goods, robot[i].x, robot[i].y, robot[i].status = map(int, input().split())
    for i in range(5):  # 5行船的信息
        boat[i].status, boat[i].pos = map(int, input().split())
    okk = input()  # 'OK'
    return id

if __name__ == "__main__":
    Init()
    for frame in range(1, 15001):
        id = Input()

        """
        这部分进行每一帧的信息处理然后给出机器人和船的运动决策
        """
        for i in range(robot_num):
            print("move", i, random.randint(0, 4))
            sys.stdout.flush()
        
        print("OK")
        sys.stdout.flush()