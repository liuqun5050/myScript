# 导入UnnitTest包
import unittest
from unittest import TestCase
from day2.test1 import Calc

ca = Calc()
# 定义一个类
class Testlx01(TestCase):

    def setUp(self):
        print("开始...")

    def test001(self):
        ca.add(10,10)
        self.assertEqual(20, 20)

    def test002(self):
        ca.sub(2,1)
        self.assertEqual(1, 1)

    def tearDown(self):
        print("结束...")

if __name__ == '__main__':
    unittest.main()
