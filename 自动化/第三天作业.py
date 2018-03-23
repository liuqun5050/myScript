# 第一题
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# url  = "https://www.baidu.com/"
# driver.get(url)
#
# el_input = driver.find_elements_by_css_selector("input")
#
# for i in el_input:
#   type = i.get_attribute("type")
#   if type != "hidden":
#    print(type)
# time.sleep(2)
# driver.close()
    # from selenium import webdriver
# driver = webdriver.Firefox()
# url = "http://www.douyu.com/directory/all"
#
# driver.get(url)
# import time
# # el = driver.find_element_by_xpath_name("shark-pager-item")
# el_1 = driver.find_element_by_xpath_class_name("shark-pager-next")
# el_1.click()
# time.sleep(3)
# 第三题
# from selenium import  webdriver
# import  time
# #创建浏览器对象
# driver=webdriver.Firefox()
# #获取指定页面
# driver.get("C:\Users\liuqun\Desktop\css_example.html")
#
# choose=""
# findby_value=""
# #进入系统的欢迎页面提示，函数
# def welcome():
#     print("********八种元素定位方式********")
#     print("1. id定位")
#     print("2. name属性值定位")
#     print("3. 伪类名定位")
#     print("4. 标签名定位")
#     print("5. 链接文本定位")
#     print("6. 部分链接文本定位")
#     print("7. xpath定位")
#     print("8. css选择器定位")
#     print("9. 退出系统")
#
# #获取用户选择的操作编号
# def get_choose():
#     choose = input("输入你要选择的定位方式(1~9):")
#     return  choose
#
# #获取用户编写的定位元素的内容
# def get_findvalue():
#     findby_value= input("请输入你的定位元素的值:")
#     return  findby_value
#
# def main_find_el():
#     while True:
#         #进入系统
#         welcome()
#         #获取用户选择的定位方式
#         choose=get_choose()
#         #id定位
#         if choose == "1":
#             findby_value = get_findvalue()
#             find_id=driver.find_element_by_id(findby_value)
#             print(find_id.get_attribute("class"))
#
#         elif choose == "2":
#             pass
#         #伪类名定位
#         elif choose == "3":
#             findby_value = get_findvalue()
#             find_id = driver.find_element_by_class_name(findby_value)
#             print(find_id.get_attribute("class"))
#         elif choose == "4":
#             pass
#         #链接文本定位
#         elif choose == "5":
#             findby_value = get_findvalue()
#             find_id = driver.find_element_by_link_text(findby_value)
#             print(find_id.text)
#         elif choose == "6":
#             pass
#         elif choose == "7":
#             pass
#         elif choose == "8":
#             pass
#         elif choose == "9":
#             break
#         # 输入错误
#         else:
#             print("你输入的数据有误，请重新输入")
#
# #开始调用函数
# # main_find_el()
#
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# url = "https://www.douyu.com/directory/all"
# driver.maximize_window()
# driver.get(url)
# el_next_page = driver.find_element_by_xpath("//*[@id='J-pager']//a[@class='shark-pager-item current']")
#
# print(el_next_page.text)
# el_next_page = driver.find_element_by_class_name("shark-pager-next")
# el_next_page.click()
# el_next_page = driver.find_element_by_xpath("//*[@id='J-pager']//a[@class='shark-pager-item current']")
# print(el_next_page.text)
# time.sleep(2)
# 第四题
from selenium import webdriver
import time
driver = webdriver.Firefox()
url  = "http://sz.58.com/"
driver.get(url)
url_1 = driver.current_url
el_click = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/a[1]")

# el_list = driver.find_elements_by_xpath("//h2/a[1]")
#
# for i in el_list:
#     print(i.get_attribute("text"))

