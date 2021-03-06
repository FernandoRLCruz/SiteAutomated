from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from page_model.product_page_model import ProductPageLocators



class ProductPage(BaseSetup, GenericMethodsClass):

    def select_product(self):
        self.scroll_into_view(By.CLASS_NAME, ProductPageLocators.selectProductByClassName)
        self.hover_over_an_element_and_click_on(By.CLASS_NAME, ProductPageLocators.hoverOverProductBoxByClassName)
        self.click_on_element(By.XPATH, ProductPageLocators.productAddButtonByXpath)

    def continue_shopping_button(self):
        element = self.is_element_visible(By.XPATH, ProductPageLocators.modalWindowByXpath)
        self.click_on_returned_element(element)
