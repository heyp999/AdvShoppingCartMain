# import sys
import datetime
from selenium import webdriver
import adshopcart_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
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
s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setup():
    print('This is automation test for Advantage Shopping Cart website')
    print(f'Test Started at: {datetime.datetime.now()}')
    print(f'--------------------------------------')
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)
    # Navigating to the website homepage
    driver.get(locators.adshopcart_url)
    # Make a full screen
    driver.maximize_window()
    assert driver.find_element(By.ID, "follow").is_displayed()  # use for judge and wait until homepage loaded completed
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and driver.title == '\xa0Advantage Shopping':
        print(f'We\'re at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We\'re seeing logo and title message -- "Advantage Shopping"')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()


# Fixture method - to close web browser
def teardown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


# Register a new user
def register_new_user():
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//span[contains(., "SIGN IN WITH FACEBOOK")]').is_displayed()
    driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()
    if not driver.find_element(By.LINK_TEXT, "CREATE ACCOUNT").is_displayed():
        print("We\'re not at the CREATE ACCOUNT page,Please Check")
        return
    driver.find_element(By.CSS_SELECTOR, "input[name='usernameRegisterPage']").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input[name='emailRegisterPage']").send_keys(locators.email)
    driver.find_element(By.CSS_SELECTOR, "input[name='passwordRegisterPage']").send_keys(locators.new_password)
    driver.find_element(By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']").send_keys(locators.new_password)
    driver.find_element(By.CSS_SELECTOR, "input[name='first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.CSS_SELECTOR, "input[name='last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.CSS_SELECTOR, "input[name='phone_numberRegisterPage']").send_keys(locators.phone)
    Select(driver.find_element(By.CSS_SELECTOR, "select[name='countryListboxRegisterPage']")).\
        select_by_visible_text('Canada')
    driver.find_element(By.CSS_SELECTOR, "input[name='cityRegisterPage']").send_keys(locators.city)
    driver.find_element(By.CSS_SELECTOR, "input[name='addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='state_/_province_/_regionRegisterPage']").send_keys(locators.province)
    driver.find_element(By.CSS_SELECTOR, "input[name='postal_codeRegisterPage']").send_keys(locators.postal_code)
    if driver.find_element(By.CSS_SELECTOR, "input[name='allowOffersPromotion']").is_selected():
        driver.find_element(By.CSS_SELECTOR, "input[name='allowOffersPromotion']").click()
    if not driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']").is_selected():
        driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']").click()
    if driver.find_element(By.ID, "register_btnundefined").is_enabled():
        driver.find_element(By.ID, "register_btnundefined").click()
    else:
        print("Something inputs is wrong,please check")
    sleep(1)
    driver.find_element(By.ID, "menuUserLink").click()
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]//label[contains(., "{locators.full_name}")]').\
            is_displayed():
        print(f"new username:'{locators.full_name}' is displayed.")
        print(f"new user account:'{locators.full_name}' is created successfully at {datetime.datetime.now()}.")
    sleep(1)
    driver.find_element(By.ID, "menuUserLink").click()
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//label[contains(., "- No orders -")]').is_displayed():
        print("We\'re seeing '- No orders' - in our account.")
    else:
        print("There are something in our account',right？")


# login with credentials(username and password)
def login(username, password):
    driver.refresh()
    driver.find_element(By.ID, 'menuUserLink').click()
    if driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
        sleep(1)
        driver.find_element(By.ID, "menuUserLink").click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//span[contains(., "SIGN IN WITH FACEBOOK")]').is_displayed()
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    if driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed():
        print(f"User:'{username}' login successfully at {datetime.datetime.now()}.")
        return True
    else:
        return False


# logout
def logout():
    driver.refresh()
    driver.find_element(By.ID, 'menuUserLink').click()
    if driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
        print(f"logout successfully:{datetime.datetime.now()}")
    else:
        print("Not logged in now")


# delete current user account, use it after login
def del_current_user():
    driver.find_element(By.ID, 'menuUserLink').click()
    if driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
        driver.find_element(By.CSS_SELECTOR, 'div[class="deleteBtnText"]').click()
        driver.find_element(By.CSS_SELECTOR, 'div[data-ng-click="deleteAccountConfirmed()"]').click()
        print(f"The User account:'{locators.new_username}' is deleted at {datetime.datetime.now()}")
    else:
        print("Can\'t delete user before login.")


# check user account is deleted successfully.
def check_user_account_deleted(username, password):
    driver.refresh()
    assert driver.find_element(By.ID, "follow").is_displayed()  # use for judge and wait until homepage loaded completed
    driver.find_element(By.ID, "menuUserLink").click()
    if driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
        sleep(1)
        driver.find_element(By.ID, "menuUserLink").click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//span[contains(., "SIGN IN WITH FACEBOOK")]').is_displayed()
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    if driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]'
                                     '[contains(., "Incorrect user name or password")]').is_displayed():
        print("We are seeing message 'Incorrect user name or password'")
        print(f"After check, User account:'{username}' is deleted successfully")
    else:
        print("After check, User account:'{username}' still alive.")


if __name__ == "__main__":
    setup()
    register_new_user()
    logout()
    login(locators.new_username, locators.new_password)
    del_current_user()
    check_user_account_deleted(locators.new_username, locators.new_password)
    teardown()
