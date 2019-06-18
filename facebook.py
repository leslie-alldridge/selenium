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

driver.get('http://facebook.com')

# email & password element on page
email_element = driver.find_element_by_xpath('.//*[@id="email"]')
password_element = driver.find_element_by_xpath('.//*[@id="pass"]')
login_button = driver.find_element_by_xpath('.//*[@id="loginbutton"]')

# send info to fields
email_element.send_keys(email)
password_element.send_keys(pw)

# login
login_button.click()

# start posting status
status_element = driver.find_element_by_xpath('//*[@name="xhpc_message"]')
time.sleep(5)

status_element.send_keys('post')
time.sleep(5)

page_buttons = driver.find_elements_by_tag_name('button')
time.sleep(5)

# find post button
for button in page_buttons:
    if button.text == 'Share':
        button.click()
