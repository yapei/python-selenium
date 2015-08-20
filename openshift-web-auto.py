from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


# environment 
URL = "https://ec2-54-160-65-173.compute-1.amazonaws.com:8443"
USERNAME = "user1"
PASSWORD = "redhat"

# Open browser
browser = webdriver.Firefox()
browser.get(URL)
time.sleep(3)
# Search 
browser.find_element_by_id('inputUsername').clear()
browser.find_element_by_id('inputUsername').send_keys(USERNAME)
browser.find_element_by_id('inputPassword').clear()
browser.find_element_by_id('inputPassword').send_keys(PASSWORD)
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)

# 'logout' element is only visible after parent button is clicked
#browser.find_element_by_xpath("//b[@class='caret']").click()
browser.find_element_by_css_selector("span.username.ng-binding").click()
browser.find_element_by_xpath("//a[@href='logout']").click()

