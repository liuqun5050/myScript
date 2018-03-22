
#导入包
from appium import webdriver

import time
#前置代码

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

#声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#通过class定位“设置”
setting_bottom = driver.find_element_by_class_name("android.widget.TextView")
#点击设置按钮
setting_bottom.click()
#通过class定位“放大镜”
search_bottom = driver.find_element_by_class_name("android.view.View")
#点击放大镜按钮
search_bottom.click()
#通过class定位“输入框”
input = driver.find_element_by_class_name("android.widget.EditText")
#在输入框中输入“无”
input.send_keys("无")

