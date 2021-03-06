import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Mytest(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test_001(self):

        driver = webdriver.Firefox()
        url = "https://www.jd.com/"
        driver.get(url)
        el_list = driver.find_elements_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li")

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
        print("test_001")
    def test_002(self):
        print("test_002")
    def test_003(self):
        print("test_003")

    def tearDown(self):
        print("teardown")
if __name__ == '__main__':
    # unittest.main()
    mysuite = unittest.TestSuite()
    mysuite.addTests(Mytest("test_001"))
    unittest.TextTestRunner(verbosity=2).run(mysuite)
