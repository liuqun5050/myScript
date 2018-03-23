# 显示提示信息
while True:
    print("1,点菜")
    print("2.呼叫服务员")
    print("3.买单")

    # 用户输入编号
    num = int(input("请输入编号"))
    if num == 1:
        print("我要点单")
    elif num == 2:
        print("呼叫服务员")
    elif num == 3:
        print("我要买单")
