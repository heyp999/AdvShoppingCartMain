import unittest
import adshopcart_methods as methods
from time import sleep
import adshopcart_locators as locators


# unittest case
class ShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_advantage_shopping_cart_case1():
        methods.setup()
        methods.check_homepage()
        methods.teardown()

    # @staticmethod
    # def test_advantage_shopping_cart_case2():
    #     methods.setup()
    #     sleep(1)
    #     methods.register_new_user()
    #     sleep(1)
    #     methods.logout()
    #     sleep(1)
    #     methods.login(locators.new_username, locators.new_password)
    #     sleep(1)
    #     methods.del_current_user()
    #     sleep(1)
    #     methods.check_user_account_deleted(locators.new_username, locators.new_password)
    #     sleep(1)
    #     methods.teardown()


if __name__ == '__main__':
    unittest.main()
