# 在百度首页上通过CSS标签定位方式定位input标签，并且证明首个input标签是name属性值为ie 的标签
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
#
# url = "https://www.baidu.com/"
# driver.get(url)
#
# el_input = driver.find_element_by_css_selector("input")
# print(el_input.get_attribute("name"))
#
# time.sleep(2)
# driver.close()
# 使用CSS定位方式依次访问sample_test,html中的元素，
# # 1.div1使用id定位方式
# # 2.div1中 p1中的a标签采用层级定位方式（多层级定位）
# # 3.最后一个a标签应该采用何种定位方式？
#
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# url = "file:///C:/Users/liuqun/Desktop/css_example.html"
# driver.get(url)
#


from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "file:///C:/Users/liuqun/Desktop/css_example.html"
driver.get(url)
el_input = driver.find_element_by_css_selector("#div1")
print(el_input.get_attribute("id"))
# el_div1 = driver.find_element_by_css_selector("#div1 a")
# print(el_div1.get_attribute("name"))
el_input = driver.find_element_by_css_selector("div p a")
print(el_input.get_attribute("text"))

el_input = driver.find_element_by_css_selector("#div2+a")
print(el_input.get_attribute("text"))

time.sleep(3)
driver.close()



