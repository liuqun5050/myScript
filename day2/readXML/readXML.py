# 导xml包
from xml.dom import minidom
# 解析文档
class ReadXML():
    def reaXML(self,one,two):
        root = minidom.parse('../DatePool/sjxXML.XML')
        # 获取文档元素
        dom = root.documentElement
        # 查找指定元素
        dys=dom,getElementsByTagName("one")[0]
        dys.getElementsByTagName("two")[0].firstChild.data
