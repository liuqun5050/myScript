from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://bj.58.com"
driver.get(url)

el_house = driver.find_element_by_link_text("个人房源")
el_house.click()

time.sleep(2)

print(len(driver.window_handles))
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)

