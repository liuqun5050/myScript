from selenium import webdriver
# from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()
url ="https://www.hao123.com/"
driver.get(url)

driver.maximize_window()
# js = "window.scrollTo(0,300)"
# time.sleep(2)
# driver.execute_script(js)
# js = "document.documentElement.scrollTop=500"
a = 1
js= "document.documentElement.scrollTop=200"
for i in js:
    a +=1
    (js = "document.documentElement.scrollTop=200")*i


    driver.execute_script(js)

time.sleep(2)
driver.close()