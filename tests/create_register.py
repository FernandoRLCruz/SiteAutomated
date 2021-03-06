from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.home_page_logado import HomeLogadoPage
import unittest


class RegisterCreateTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(RegisterCreateTest, self).setUp()
        self.home_page = HomePage(self.driver)
        self.home_page_logado = HomeLogadoPage(self.driver)

    def test_create_register(self):
        self.home_page.registerAction()
        result = self.home_page_logado.getTextLabel()
        self.assertEqual(result, "MY ACCOUNT")



if __name__ == '__main__':
    unittest.main()
