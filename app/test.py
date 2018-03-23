import time
#导入包
from appium import webdriver

#import time
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

#通过xpath定位“设置”
setting_bottom = driver.find_element_by_xpath("//*[contains(@text,'设置')]")
#点击设置按钮
setting_bottom.click()
#通过id定位“放大镜”
search_bottom = driver.find_element_by_id("com.android.settings:id/search")
#点击放大镜按钮
search_bottom.click()
#通过id定位“输入框”
input_text= driver.find_element_by_id("android:id/search_src_text")

#在输入框中输入“无”
input_text.send_keys("无")
#打印文本
text_name =  driver.find_elements_by_id("com.android.settings:id/title")

for i in text_name:
    print(i.text)
print(len(text_name))




