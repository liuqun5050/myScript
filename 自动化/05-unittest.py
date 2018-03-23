import seleniumcommon
import HTMLTestRunner
import unittest
import time

class Mytest(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test_001(self):
        browser = seleniumcommon.Common()
        browser.open_url("http://www.yhd.com/")
        browser.myclick("class", "hd_login_link")
        time.sleep(2)
        browser.mysend_keys("id", "un", "hack_ai_buster")
        browser.mysend_keys("id", "pwd", "1qaz2wsx#EDC")
        browser.myclick("id", "login_button")
        time.sleep(2)

        # 验证是否登录成功
        # browser.get_text("class", "hd_login_name")
        self.assertEqual("hack_ai_buster", browser.get_text("class", "hd_login_name"))

    def test_002(self):
        print("test 002")
    def tearDown(self):
        print("teardown")

class Mytest2(unittest.TestCase):
    def test_001(self):
        print("test 201")
    def test_002(self):
        print("test 202")

if __name__ == '__main__':
    # unittest.main()
    mysuite = unittest.TestSuite()
    mysuite.addTest(Mytest("test_001"))

    # unittest.TextTestRunner(verbosity=2).run(mysuite)
    with open("firstreport.html", "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream = f, title = "第一份报告", description="测试用例执行").run(mysuite)