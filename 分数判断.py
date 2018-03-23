#判断分数等级

# score = int(input("请输入分数"))
score = (input("请输入分数"))
print (len(score))
print(type(score))
if 100 >= score >= 80:
# if "80" score "100":
    print(type(score))
    print("优秀")
elif 79 >= score >= 60:
    print("良好")
elif 60 > score:
    print("不及格")
else:
    print("输入错误")



