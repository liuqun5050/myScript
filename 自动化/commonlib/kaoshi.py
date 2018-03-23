import HTMLTestRunner
import seleniumcommon
import unittest
import time


class Mytest(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_001(self):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        import time
        driver = webdriver.Firefox()
        # 打开百度
        url = "http://www.baidu.com"
        driver.get(url)

        # 定位到设置，并鼠标悬停
        el_set = driver.find_element_by_link_text("设置")
        action = ActionChains(driver)
        action.move_to_element(el_set).perform()

        # 定位到搜索设置
        el_search_set=driver.find_element_by_link_text("搜索设置")
        el_search_set.click()

        # 定位到保存设置
        el_save_set = driver.find_element_by_link_text("保存设置")
        el_save_set.click()

        # 弹出窗口

        alert = driver.switch_to.alert
        print(alert.text)
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        driver.close()

    def test_002(self):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        import time

        # 获取浏览器对象，打开网页
        driver = webdriver.Firefox()
        url = "https://www.jd.com/"
        driver.get(url)
        # 鼠标悬停位置
        el_list= driver.find_elements_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li")

        a = 0
        for i in el_list:
            a += 1
            if a <= 5:
                action = ActionChains(driver)
                action.move_to_element(i).perform()
                time.sleep(2)
            else:
                break
        driver.close()
    def tearDown(self):
        print("teardown")

if __name__ == '__main__':
    mysuite = unittest.TestSuite()
    mysuite.addTest(Mytest("test_001"))
    mysuite.addTest(Mytest("test_002"))
    unittest.TextTestRunner(verbosity=2).run(mysuite)
    with open("first.html", "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream = f, title = "第一份报告", description="测试用例执行").run(mysuite)