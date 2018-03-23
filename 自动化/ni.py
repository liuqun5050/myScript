import  seleniumcommon
import HTMLTestRunner
import unittest
import time

class Mytest(unittest.TestCase):
    def setUp(self):
        print("setup")


    def test_001(self):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        import time
        driver=webdriver.Firefox()
        url="http://www.baidu.com"
        driver.get(url)
        driver.maximize_window()

        #鼠标在设置文本位置悬停
        action=ActionChains(driver)
        #设置元素定位

        el=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]")
        #鼠标悬停

        action.move_to_element(el).perform()
        time.sleep(2)

        #在悬停时，鼠标悬停移动到搜索设置文本，再点击进入搜索设置页面
        #鼠标在搜索设置文本停留
        el2=driver.find_element_by_link_text("搜索设置")
        el3=action.move_to_element(el2).perform()
        time.sleep(2)

        #鼠标点击
        el2.click()

        #点击保存设置，在进行弹出框操作
        el4=driver.find_element_by_link_text("保存设置")
        action.move_to_element(el4).perform()
        el4.click()
        time.sleep(3)

        #先进入弹出框，在选择弹出框操作
        el5=driver.switch_to.alert
        print(el5.text)
        el5.accept()
        time.sleep(2)

        driver.quit()
    def tearDown(self):
        print("teardown")

    def test_002(self):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        import time

        driver = webdriver.Firefox()

        url = "http://www.jd.com"

        driver.get(url)
        driver.maximize_window()
        #定义停留模块的所有元素
        el = driver.find_elements_by_css_selector(".cate_menu_item")
        #用for循环在模块中依次在五个的文本中鼠标悬停，
        for i in range(5):
            el_word = el[i]
            ActionChains(driver).move_to_element(el_word).perform()
            time.sleep(2)

        driver.quit()


if __name__ == '__main__':
    #定义需要执行的测试用例
    mysuite = unittest.TestSuite()
    mysuite.addTest(Mytest("test_001"))
    mysuite.addTest(Mytest("test_002"))
    #将执行成功的测试用例，编写成二进制的html文件，并写入html文件的名字，html页面标题，测试用例的描述
    with open("firstreport.html", "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream = f, title = "第一份报告", description="测试用例执行").run(mysuite)