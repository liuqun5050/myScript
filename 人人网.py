from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://www.renren.com"
driver.get(url)
el_user = driver.find_element_by_name("email")
el_user.send_keys("17173805860")
el_pwd = driver.find_element_by_name("password")
el_pwd.send_keys("lqaz@wsx3edc")
el_login = driver.find_element_by_id("login")

time.sleep(2)
driver.close()