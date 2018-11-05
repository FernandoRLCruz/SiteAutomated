import time
from random import randint

from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from page_model.home_page_model import HomePageLocators
from page_model.order_page_model import OrderPageLocators
from utilities.data import info_user, products_list
from base.product import Product


class OrderPage(BaseSetup, GenericMethodsClass):

    def clickProceedCheckoutSummary(self):
        self.is_element_visible(By.XPATH, OrderPageLocators.proceedCheckoutSummaryButtonByXpath)
        self.click_on_element(By.XPATH, OrderPageLocators.proceedCheckoutSummaryButtonByXpath)

    def clickProceedCheckoutAddress(self):
        self.is_element_visible(By.NAME, OrderPageLocators.proceedCheckoutAddressButtonByName)
        self.click_on_element(By.NAME, OrderPageLocators.proceedCheckoutAddressButtonByName)

    def clickProceedCheckoutShipping(self):
        self.is_element_visible(By.NAME, OrderPageLocators.proceedCheckoutShippingButtonByName)
        self.click_on_element(By.NAME, OrderPageLocators.proceedCheckoutShippingButtonByName)

    def clickProceedCheckoutPayment(self):
        self.is_element_visible(By.XPATH, OrderPageLocators.payByBankCheckoutPaymentByXpath)
        self.click_on_element(By.XPATH, OrderPageLocators.payByBankCheckoutPaymentByXpath)

    def clickProceedCheckoutTermsService(self):
        self.driver.implicitly_wait(5)
        element = self.find_element(By.ID, OrderPageLocators.termsServiceCheckoutAddressButtonByID)
        self.driver.execute_script("arguments[0].click();", element)

    def clickProceedCheckoutConfirmOrder(self):
        self.is_element_visible(By.XPATH, OrderPageLocators.confirmOrderButtonByXpath)
        self.click_on_element(By.XPATH, OrderPageLocators.confirmOrderButtonByXpath)

    def getTextLabelConfirmOrder(self):
        self.is_element_visible(By.XPATH, OrderPageLocators.orderConfirmLabelByXpath)
        element = self.find_element(By.XPATH, OrderPageLocators.orderConfirmLabelByXpath)
        return element.text

    def getTextLabelValueOrder(self):
        self.is_element_visible(By.XPATH, OrderPageLocators.priceFinalOrderLabelByXpath)
        element = self.find_element(By.XPATH, OrderPageLocators.priceFinalOrderLabelByXpath)
        element = int(element.text[1:3])
        return element

    def getTextLabelValueShippingOrder(self):
        self.is_element_visible(By.ID, OrderPageLocators.shippingCheckoutLabelByID)
        element = self.find_element(By.ID, OrderPageLocators.shippingCheckoutLabelByID)
        element = int(element.text[1:2])
        return element

    def orderCreate(self):
        self.shipping = self.getTextLabelValueShippingOrder()
        self.clickProceedCheckoutSummary()
        self.clickProceedCheckoutAddress()
        self.clickProceedCheckoutTermsService()
        self.clickProceedCheckoutShipping()
        self.clickProceedCheckoutPayment()
        self.clickProceedCheckoutConfirmOrder()
        self.getTextLabelConfirmOrder()
