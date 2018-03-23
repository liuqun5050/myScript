# 需求：定一个函数，完成对一个工资计算税额
# 定义一个函数
def count(a):

    b = a * 0.1
    return b


a = int(input("请输入你的工资"))
c = count(a)

# print("你本月的工资为：%d,应交税额为:%d" % (x, y))
print("您的本月工资是：%d，应该交税的额是：%f" % (a, c))