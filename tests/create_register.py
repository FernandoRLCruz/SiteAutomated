from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.dresses_page import DressesPage
from pages.shopping_cart_page import ShoppingCartPage
import unittest


class RegisterCreateTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(RegisterCreateTest, self).setUp()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.dresses_page = DressesPage(self.driver)

    def test_create_register(self):
        self.home_page.registerAction()


if __name__ == '__main__':
    unittest.main()
