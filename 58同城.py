from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://sz.58.com/"
driver.get(url)

el_rent = driver.find_element_by_partial_link_text("房屋出租")

el_rent.click()
time.sleep(3)
driver.quit()