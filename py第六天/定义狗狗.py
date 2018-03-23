# 定义一个类
class Dog(object):

    def eat(self):
        print("狗在吃饭")
    def drink(self):
        print("%s在喝水" %self.name)

    def __init__(self,new_name,new_age,new_color):
        self.name = new_name
        self.age = new_age
        self.color = new_color
        # print("%s的颜色是:%s,年龄是:%d" % (self.name, self.color, self.age))

# 定义对象
# dog1 = Dog()
dog1 = Dog ("小黄",2,"yellow")

# dog1.color = "yellow"
# dog1.age = 2
# dog1.name = "小黄"
# dog2 = Dog()
dog2 = Dog ("小黑",1,"black")
# dog2.self_instrodution ("小黑",1,"black")

# dog2.color = "black"
# dog2.age = 1
# dog2.name = "小黑"
#

# dog1.drink()

