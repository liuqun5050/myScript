# 要求：定一个函数返回对3的商以及余数

# 定义一个函数
def get_result(a):
    b = a // 3
    c = a / 3
    return c,b

num = get_result(int(input("请输入数字")))
print(num)