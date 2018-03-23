from selenium import webdriver
import time

class Common(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def mysend_keys(self, type, value, data):
        self.location_func(type, value).send_keys(data)

    def myclick(self, type, value):
        self.location_func(type, value).click()

    def get_text(self, type, value):
        return self.location_func(type, value).text

    def location_func(self, type, value):
        el = None
        if type == "id":
            el = self.driver.find_element_by_id(value)
        if type == "class":
            el = self.driver.find_element_by_class_name(value)
        if type == "name":
            el = self.driver.find_element_by_name(value)
        if type == "tag":
            el = self.driver.find_element_by_class_tag_name(value)
        if type == "link_text":
            el = self.driver.find_element_by_link_text(value)
        if type == "partial_link_text":
            el = self.driverr.find_element_by_partial_link_text(value)
        if type == "css":
            el = self.driver.find_element_by_css_selector(value)
        if type == "xpath":
            el = self.driver.find_element_by_class_xpath(value)

        return el

if __name__ == '__main__':
    browser = Common()
    browser.open_url("http://www.baidu.com")
    browser.mysend_keys('id', 'kw', "selenium")
    time.sleep(1)
