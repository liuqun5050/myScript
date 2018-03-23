from selenium import webdriver
# from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
url = "https://www.qunaer.com/"
driver.get(url)
# el_list = driver.find_elements_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li")
#
# a = 0
# for i in el_list:
#     a +=1
#     if a <=5:
#         action = ActionChains(driver)
#         action.move_to_element(i).perform()
#         time.sleep(2)
#     else:
#         break

driver.sleep(2)


driver.close()