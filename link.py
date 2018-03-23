url_list=

for url in url_list:

    driver.get(url)
    time.sleep(1)

for i in range(2):

    driver.back()
    time.sleep(1)