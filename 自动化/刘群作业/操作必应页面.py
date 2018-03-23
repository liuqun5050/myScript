from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
url = "file:///C:/Users/liuqun/Desktop/iframe_switch/example_frame.html"
driver.get(url)



el_frame = driver.find_element_by_id("itcast_frame1")
driver.switch_to.frame(el_frame)
el_frame1 = driver.find_element_by_id("itcast_frame2")
driver.switch_to.frame(el_frame1)
el_input = driver.find_element_by_id("sb_form_q")
el_input.send_keys("python")
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()
print(driver.find_element_by_tag_name("h3").text)
time.sleep(2)
driver.close()