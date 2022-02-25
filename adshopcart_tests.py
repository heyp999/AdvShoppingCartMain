import unittest
import adshopcart_methods as methods
from time import sleep


# unittest case
class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_advantage_shopping_cart():
        methods.setUp()
        sleep(2)
        # methods.log_in(locators.moodle_username, locators.moodle_password)
        # methods.create_new_user()
        # methods.check_user_created()
        # methods.log_out()
        # methods.log_in(locators.new_username, locators.new_password)
        # methods.check_we_logged_in_with_new_cred()
        # methods.log_out()
        # methods.log_in(locators.moodle_username, locators.moodle_password)
        # methods.delete_test_user()
        # methods.log_out()
        methods.tearDown()
