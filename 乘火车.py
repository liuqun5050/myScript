# 1.检查是否购买车票，2.过安检 3.两项都能通过，就可以乘车
# 1.获取用户信息
ticket = input("请问是否购票")
# 2.检票
if ticket == "yes":
    print("可以进入车站")
    print("接下来进入安检")
# 3.获取用户物品信息
    knife = input("请问有携带长过10cm的道具吗")
    if  knife == "no":
         print("通过安检")
         print("进入候车厅")
    else:
         print("没有通过安检")
         print("请等待经常处理")
else:
     print("请补票")

