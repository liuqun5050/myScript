# 1.设置一个行的变量
i = 1
# 2.控制行数
while i <= 9:
# 3.设置一个列的变量
    j = 9
# 4.控制列数
    while j >= i:

        print("*",end="")
        j -= 1

    print("")
    i += 1