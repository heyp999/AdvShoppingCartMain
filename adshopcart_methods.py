import sys
import datetime
from selenium import webdriver
import adshopcart_locators as locators
# from time import sleep
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# -------------for run in the background--------------
# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(options=options)
# -------------for run in the background--------------
driver = webdriver.Chrome()


# Fixture method - to open web browser
def setUp():
    print('This is automation test for Advantage Shopping Cart website')
    print(f'Test Started at: {datetime.datetime.now()}')
    print(f'--------------------------------------')
    # Make a full screen
    driver.maximize_window()
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)
    # Navigating to the Moodle app website
    driver.get(locators.adshopcart_url)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and driver.title == '\xa0Advantage Shopping':
        print(f'We\'re at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We\'re seeing logo and title message -- "Advantage Shopping"')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()


# Fixture method - to close web browser
def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
