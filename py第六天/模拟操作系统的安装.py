class MiniOs(object):
    """定义一个类，模拟操作系统"""
    def __init__(self, name):
        self.name = name
        self.app_name = []

    def __str__(self):
        return "操作系统的名字是%s,已安装的软件是%s"  %(self.name,self.app_name)

    def install_app(self,app_temp):
        if app_temp.name not in self.app_name:
            app_temp.install()
            self.app_name.append(app_temp.name)
        else:
            print("请卸载后重装")


class app(object):
    """定义一个类，管理所有软件的信息"""
    def __init__(self,name,version,desc):
        self.name = name
        self.version = version
        self.desc = desc

    def install(self):
        print("正在安装%s到C盘" %self.name)



class qq(app):
    pass


class weixin(app):
    def install(self):
        print("正在安装%s到e盘" %self.name)


class pycharm(app):
    pass




QQ = qq("2017版QQ", "v8", "用来聊天")
Weichat =  weixin("2017版本微信","v8","用来聊天")
Pycharm =  pycharm("2017版本Pycharm","v8","用来写代码")


QQ.install()
Weichat.install()
Pycharm.install()
# 创建一个操作系统对象

mini_os = MiniOs("minios17版")
print(mini_os)


mini_os.install_app(QQ)
mini_os.install_app(Weichat)
mini_os.install_app(Pycharm)

print(mini_os)