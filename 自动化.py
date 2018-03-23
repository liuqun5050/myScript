from selenium import webdriver
import time
driver = webdriver.Firefox()
#
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# # 获取页面大小
# size = driver.get_window_size()
# print(size)
#
# # print(driver.set_window_size(300,500))
#
# print(driver.get_window_position())
# driver.set_window_position(200,200)
# time.sleep(3)
#
# driver.close()


# url = "http://www.baidu.com"
# driver.get(url)
#
# el_input = driver.find_element_by_id("kw")
#
# el_input.send_keys("传智播客")
# time.sleep(2)
# driver.close()

url = "https://www.qunar.com"

driver.get(url)

el = driver.find_element_by_id("__link_travel__")
print(el.get_attribute("id"))
el.click()

time.sleep(2)
driver.close()