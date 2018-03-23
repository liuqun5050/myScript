# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
# driver = webdriver.Firefox()
# url = "http://www.baidu.com"
# driver.get(url)
# # 定位Logo图标
# el_logo = driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[1]/div/div[1]/map/area")
# # 右键点击
# action = ActionChains(driver)
# action.context_click(el_logo).perform()
# # 悬停鼠标
# #-------------------
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
# driver = webdriver.Firefox()
# url = "http://www.baidu.com"
# driver.get(url)
# el_sz = driver.find_element_by_link_text("设置")
# action = ActionChains(driver)
# action.move_to_element(el_sz).perform()
# time.sleep(2)
# driver.close()
#
# 鼠标定位输入关键词
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
url = "http://www.baidu.com"
driver.get(url)

el_input = driver.find_element_by_id("kw")
action = ActionChains(driver)
action.send_keys_to_element(el_input,"python").perform()

time.sleep(2)
driver.close()