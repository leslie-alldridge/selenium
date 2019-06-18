from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pw import pw, email
import time

# set up driver & get facebook
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

driver.get('https://status.newrelic.com/')
sleep(4)
title = driver.find_element_by_xpath('//*[@id="past-incidents"]')
title.click()
outage_elements = driver.find_elements_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/*')

for element in outage_elements:

    print(element.text)
# /html/body/div[1]/div[2]/div[3]/div[10]/p

# /html/body/div[1]/div[2]/div[3]/div[12]/p

# /html/body/div[1]/div[2]/div[3]/div[1]/p
