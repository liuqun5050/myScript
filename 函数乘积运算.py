# 求两个数字差的乘积

# 设定一个差的乘积函数
while True:
    def jian_result():
    # 设置两个值
        a = int(input("请输入第一个数字"))
        b = int(input("请输入第二个数字"))

    # 设置一个变量来存储2个值相减的结果
        c = a - b
    # 返回结果
        return c
    # 设定一个乘积的函数
    def chengji_result():
        a = jian_result()
        b = a * a
        # print(b)
        return b
    # 求立方和平方的差
    def fan_result():
        c = jian_result()
        a = c * c * c
        b = c * c
        d = a - b
        print(d)
        return d


    fan_result()
    # print(e)




    # d = jian_result()
    # chengji_result(d)