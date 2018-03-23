# -*- coding: utf-8 -*-
#导入包
from appium import webdriver
#前置代码
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#声明对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#通过xpath定位“设置”
setting_bottom = driver.find_element_by_xpath("//*[contains(@text,'设置')]")
#点击设置按钮
setting_bottom.click()
#获取文本信息
text_name = driver.find_elements_by_class("android.widget.TextView")
for i in text_name:
    if i.text == "关于手机":
        #获取“关于手机的属性”
        text_value = driver.find_element_by_xpath("//*[contains(@text,'关于手机')]")
        text_value.click()
        text_value2 = driver.find_elements_by_class("android.widget.TextView")
        for a in text_value2:
            if a.text == "5.1":
                print(a.text)


