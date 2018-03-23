from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)

el_input = driver.find_element_by_id("kw")
el_input.send_keys("python")
el_input.send_keys(Keys.CONTROL,'a')
el_input.send_keys(Keys.CONTROL,'x')
el_input.send_keys(Keys.CONTROL,'v')
time.sleep(2)
driver.close()