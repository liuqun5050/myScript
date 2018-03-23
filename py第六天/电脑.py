class computer(object):
    def __init__(self,name):
        self.name = name

    def watch_tv(self):
        print("%s:可以看电视" %self.name)

    def work(self):
        print("%s:我可以用来工作" %self.name)


class phone(computer):
    def call(self):
        print("我可以打电话")


class ipad(phone):
    def play_game(self):
        print("我可以打游戏")


class person(object):
    def __init__(self,name):
        self.name = name
        # self.product = []

    # def have_prduct(self,product_temp):
    #     print("-----");
    #     self.product.append(product_temp.name)

    def use_product(self,product_temp):
        print("%s想打游戏" %self.name)
        product_temp.play_game()


Computer = computer("我是电脑")
ipone = phone("我是手机")
Ipad = ipad("我是平板")
baby = person("宝宝")
baby.use_product(Ipad)




