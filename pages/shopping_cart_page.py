from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from page_model.shoppingCart_page_model import ShoppingCartPageLocators


class ShoppingCartPage(BaseSetup, WebDriverCustomClass):

    def cart_products(self, item):
        return self.find_elements(By.LINK_TEXT, ShoppingCartPageLocators.pinnedChiffonDress)
