# 设计一个动物类，属性有名称、颜色、性别，方法有吃、跑，然后创建一个小猫对象，调用吃和跑方法，
# 并提供类属性、实例属性、类方法、实例方法、静态方法。
class animal(object):

    def __init__(self,name,color,sex):
        self.name = name
        self.color = color
        self.sex = sex

    def eat(self,name):
        print("---%s-我会吃----" %self.name)

    def run(self,name):
        print("---%s-我会跑----" % self.name)



# class cat(animal):
    # def __int__(self,name):
    #     self.name = name

    # def print(self,temp):
    #
    #     # print("--%s会%s--会%s" %self.name,temp)
    #
    #     print("--%s会跑--%s会走" % self.name)





cat  =  animal("a","black","nv")

cat.eat()
cat.run()
