from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from page_model.product_page import ProductPageLocators



class ProductPage(BaseSetup, WebDriverCustomClass):

    def select_product(self):
        self.scroll_into_view(By.CLASS_NAME, ProductPageLocators.selectProductByClassName)
        self.hover_over_an_element_and_click_on(By.CLASS_NAME, ProductPageLocators.hoverOverProductBoxByClassName)
        self.click_on_element(By.XPATH, ProductPageLocators.productAddButtonByXpath)

    def continue_shopping_button(self):
        element = self.is_element_visible(By.XPATH, ProductPageLocators.modalWindowByXpath)
        self.click_on_returned_element(element)
