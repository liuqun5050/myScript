from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)

el_set = driver.find_element_by_link_text("设置")
action = ActionChains(driver)
action.move_to_element(el_set).perform()
el_search_set = driver.find_element_by_link_text("搜索设置")
el_search_set.click()
el_save_set = driver.find_element_by_link_text("保存设置")
el_save_set.click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
time.sleep(2)

driver.close()
