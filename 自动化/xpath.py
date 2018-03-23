# # 多元素查找
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# url = "file:///C:/Users/liuqun/Desktop/css_example.html"
# driver.get(url)
# el_list = driver.find_elements_by_tag_name("p")
    # print(len(el_list))
# for el in el_list:
#     print(el.get_attribute("class"))
#
# driver.close()

# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# url = "https://www.baidu.com/"
# driver.get(url)
# el_input = driver.find_element_by_id("kw")
# el_input.send_keys("python")
#
# el_click= driver.find_element_by_id("su")
# el_click.click()
#
# time.sleep(2)
# driver.close()
from selenium import webdriver
import time
driver = webdriver.Firefox()
url  = "https://www.baidu.com/"
driver.get(url)
el_input = driver.find_element_by_id("kw")
el_input.send_keys("python")
el_click= driver.find_element_by_id("su")
el_click.click()
url_1 = driver.current_url
driver.get(url_1)
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# url = "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=python"
# driver.get(url)
el_list = driver.find_elements_by_xpath("//h3/a")

# el_link = driver.find_element_by_partial_link_text()
print(len(el_list))
for el in el_list:
    print(el.get_attribute("text"))