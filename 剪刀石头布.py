# 剪刀（0）石头（1）布（2）
#
# 让机器模拟一个随机数据
# import random
# a = random.randint(0,2)
# a = 0
while True:
    player = int(input("请出拳"))
    a = int(input("请出拳"))
    if player == a:
        print("平局")
    elif (player == 0 and a == 2) or (player ==1 and a == 0) or (player == 2 and a ==1):
        print("我赢啦")
    else:
        print("输啦，不开心")