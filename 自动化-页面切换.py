from selenium import webdriver
import time
driver = webdriver.Firefox()

link = ["http://www.baidu.com","http://zhuanlan.zhihu.com","http://www.hao123.com"]
i = 1
while i < 3:
    i+= 1

    driver.get(link[0])
    time.sleep(5)

    driver.get(link[1])
    time.sleep(5)

    driver.back()
    time.sleep(5)

    driver.get(link[2])
    time.sleep(5)

    driver.back()
    time.sleep(5)


