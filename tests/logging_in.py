from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.home_page_logado import HomeLogadoPage
from pages.login_page import LoginPage
import unittest


class LoggingInTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(LoggingInTest, self).setUp()
        self.home_page = HomePage(self.driver)
        self.home_page_logado = HomeLogadoPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_logging_in(self):
        self.home_page.clickLoginButton()
        self.login_page.loginSuccessful()
        result = self.home_page_logado.getTextLabel()
        self.assertEqual(result, "MY ACCOUNT")




if __name__ == '__main__':
    unittest.main()
