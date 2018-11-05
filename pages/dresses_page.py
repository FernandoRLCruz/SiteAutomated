from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from utilities.helpers import wait_and_click
import time
from page_model.dresses_page_model import DressesPageLocators


class DressesPage(BaseSetup, GenericMethodsClass):




    def add_to_the_cart_all_products_in_the_category(self):
        counter = 1
        self.scroll_into_view(By.XPATH, DressesPageLocators.scrollIntoViewByXpath)
        components = self.find_elements(By.XPATH, DressesPageLocators.hoverAllElementsByXpath)
        for element in components:
            time.sleep(.5)
            self.hover_over_an_element(element,By.XPATH,
                                       DressesPageLocators.locateSelectedElementsByXpath)
            wait_and_click(self, By.XPATH, DressesPageLocators.productAddButtonByXpath)
            counter += 1
            wait_and_click(self, By.XPATH, DressesPageLocators.modalWindowByXpath)
