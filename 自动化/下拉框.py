from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()
url ="file:///C:/Users/liuqun/Desktop/select.html"
driver.get(url)

# 1.定位下拉框标签

el_sel = driver.find_element_by_tag_name("select")
# 2.选择下拉框
seobj = Select(el_sel)
seobj.select_by_visible_text("深圳")
time.sleep(2)
seobj.select_by_index(0)
time.sleep(2)
seobj.select_by_value("3")
time.sleep(2)


print(seobj.first_selected_option.text)
for i in seobj.options:
    print(i.text)
    print(i.get_attribute("value"))
driver.close()



