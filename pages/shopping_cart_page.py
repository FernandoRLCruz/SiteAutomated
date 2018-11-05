from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from page_model.shoppingCart_page_model import ShoppingCartPageLocators


class ShoppingCartPage(BaseSetup, GenericMethodsClass):

    def cart_products(self, item):
        return self.find_elements(By.LINK_TEXT, ShoppingCartPageLocators.pinnedChiffonDress)
