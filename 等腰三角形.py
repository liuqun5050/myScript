# 给行一个变量
a = 4
i = 1
# 控制行数
while i <= a:
# 给列一个变量
    j = 2 * a -1;
# 控制列数
    x = i - 1;
    while x > 0:
        print(" ", end="")
        x -= 1;
    while j > (i - 1) * 2:
        print("*",end="")
        j -= 1
    print("")
    i += 1


