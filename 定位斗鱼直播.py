from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://www.douyu.com/directory/all"

driver.get(url)

i = 0
while i < 3:
    i+= 1
    el = driver.find_element_by_class_name("shark-pager-next")
    el.click()
    time.sleep(3)

    driver.close()
from selenium import webdriver
driver = webdriver.Firefox
url = ""