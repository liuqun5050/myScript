# 名字管理系统
# 1.可以添加姓名
# 2.可以删除姓名
# 3.可以查询是否存在某个姓名
# 4.可以修改名字
# 5.可以循环执行
# 6.退出系统系统化
# 1,输入提示信息
print("1,显示全部名字")
print("2.增加一个名字")
print("3.删除一个名字")
print("4.修改一个名字")
print("5.修改一个名字")
# 创建一个列表
names = []
# 请输入你要输入的编号
num = input("请输入编号")
if num == "1":
    print(names)
elif num == "2":
    new_name = input("请输入姓名")
    names.append(new_name)
    print(names)

# elif num == "3":
#     请输入想要删除的名字
#     del_name = input("请输入想要删除的名字")
#     确认是否要删除这个名字
#     del_name1 = input("请输入想要删除的名字:yes,or no")
#     if del_name1 = "yes":
#         names.remove(del_name)
#         print(names)
elif num == "4":
    # 输入要修改的名字
    old_name = input("请输入要修改的名字")
    # 确定要修改名字吗
    new_name = input("请输入要修改成的新名字")
    # 确定是否修改
    new_name1 = input("确定要修改吗，yes or no")
    if new_name == "yes":
        names[names.index(old_name)] = new_name
  查询
  elif num == "5"
 输入要查询的姓名
 rea_name = input(输入要查找的姓名)
    if rea_name in names:


