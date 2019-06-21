from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# set up driver & get facebook
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

driver.get('https://central.xero.com/s/question/0D51N00004XQXg5SAH/xero-support ')
sleep(3)
# go to lauren
authors = driver.find_elements_by_css_selector("span[data-id='005o0000002mTivAAE']")

if authors:
    count = 0
    # go to each post
    for author in authors:
        if 'Lauren' in author.text:
            # scroll into view
            sleep(2)
            author.location_once_scrolled_into_view

            # expand post if it exists
            try:
                print('hitting try')
                link = driver.find_element_by_link_text('Expand Post')
                link.click()
                driver.save_screenshot('image_' + str(count) + '.png')
                count += 1
            except :
                print('hitting except')
                driver.save_screenshot('image_' + str(count) + '.png')
                count += 1
        else: pass
            
        
        
else:
    driver.close()

