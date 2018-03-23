from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "https://mail.163.com/"
driver.get(url)

el_frame = driver.find_element_by_id("x-URS-iframe")
driver.switch_to.frame(el_frame)
el_input = driver.find_element_by_name("email")
el_input.send_keys("liuqun5050")

el_pw = driver.find_element_by_name("password")
el_pw.send_keys("505911")

el_dl = driver.find_element_by_id("dologin")
el_dl.click()

driver.switch_to.parent_frame()

time.sleep(2)
driver.close()