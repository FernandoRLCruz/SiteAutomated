from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.home_page_logado import HomeLogadoPage
from pages.login_page import LoginPage
import unittest

from pages.order_page import OrderPage


class PaymentOneItemTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(PaymentOneItemTest, self).setUp()
        self.home_page = HomePage(self.driver)
        self.home_page_logado = HomeLogadoPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.order_page = OrderPage(self.driver)


    def test_payment_one_item(self):
        self.home_page.clickLoginButton()
        self.login_page.loginSuccessful()
        self.home_page.addInCart()
        self.order_page.orderCreate()
        resultText = self.order_page.getTextLabelConfirmOrder()
        resultValue = self.order_page.getTextLabelValueOrder()
        resultShipping = self.order_page.shipping
        self.assertEqual(resultText, "Your order on My Store is complete.")
        self.assertEqual(self.home_page.cartValue + resultShipping, resultValue)




if __name__ == '__main__':
    unittest.main()
