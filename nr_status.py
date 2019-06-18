import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pw import pw, email

# set up driver & get facebook
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

driver.get('https://status.newrelic.com/')
session_id = driver.session_id
print(driver.session_id)
sleep(4)
title = driver.find_element_by_xpath('//*[@id="past-incidents"]')
title.click()
print(driver.session_id)

outage_elements = driver.find_elements_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/*/*/*/a')

json_blob = {"data": []}
length = len(outage_elements)
count = 0

while count < length:
    try:
        outage_elements = driver.find_elements_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/*/*/*/a')
        outage_elements[count].click()
        sleep(1)
        current_url = driver.current_url
        driver.get(current_url + '.json')
        json_body = driver.find_element_by_xpath('/html/body/pre')
        json_blob["data"].append(json_body.text)
        print(json_blob)
        driver.get('https://status.newrelic.com/')
        sleep(1)
        title = driver.find_element_by_xpath('//*[@id="past-incidents"]')
        title.click()
        sleep(4)
        count += 1
    except:
        raise Exception('We could not find that element')

print(json_blob)

with open('data.json', 'w') as json_file:
    # data = json.loads(json_blob)
    json.dump(json_blob['data'], json_file)
    print('data saved')

# end session
driver.close()
