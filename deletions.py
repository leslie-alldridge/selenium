from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from slack import sendSlack, createSlackThread, createDelSlackThread, sendSlackDel

# set up driver & get url
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

# open file with URLs
f=open("deletion-urls.txt", "r")
web_urls = f.read().splitlines()

session_id = driver.session_id
count = 0

thread = createDelSlackThread()

# go to each url and find Laurens posts
for url in web_urls:
    # maintain the same session
    driver.session_id = session_id
    driver.get(url)
    sleep(3) 

    # get laurens posts
    authors = driver.find_elements_by_css_selector("span[data-id='005o0000002mTivAAE']")
    # get Kavi posts
    authors.extend(driver.find_elements_by_css_selector("span[data-id='005o0000001zIayAAE']"))
    # get Kelly posts
    authors.extend(driver.find_elements_by_css_selector("span[data-id='005o0000001zIb3AAE']"))

    # take photo
    image_name = 'image_' + str(count) + '.png'
    driver.save_screenshot(image_name)
    count += 1
    sendSlackDel(image_name, url, '-- First post of thread -- ', thread['ts'])

    if authors:
        
        # go to each post
        for author in authors:
            if 'Lauren Costello' in author.text:
                # create backup thread
                
                print(thread)
                # scroll into view
                sleep(1)
                author.location_once_scrolled_into_view

                

                # expand post if it exists
                try:
                    link = driver.find_element_by_link_text('Expand Post')
                    link.click()
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Lauren', thread['ts'])
                except :
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Lauren', thread['ts'])
            
            elif 'Kavithya' in author.text:
                 # create backup thread
                
                print(thread)
                # scroll into view
                sleep(1)
                author.location_once_scrolled_into_view

                # expand post if it exists
                try:
                    link = driver.find_element_by_link_text('Expand Post')
                    link.click()
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Kavi', thread['ts'])
                except :
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Kavi', thread['ts'])
            
            elif 'Kelly Munro' in author.text:
                 # create backup thread
                
                print(author)
                # scroll into view
                sleep(1)
                author.location_once_scrolled_into_view

                # expand post if it exists
                try:
                    link = driver.find_element_by_link_text('Expand Post')
                    link.click()
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Kelly', thread['ts'])
                except :
                    image_name = 'image_' + str(count) + '.png'
                    driver.save_screenshot(image_name)
                    count += 1
                    sendSlack(image_name, url, 'Kelly', thread['ts'])
            
            else: pass
                
            
    else:
        print('No author found')
driver.close()

print('Done')

