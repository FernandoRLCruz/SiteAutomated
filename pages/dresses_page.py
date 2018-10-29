from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.helpers import wait_and_click
import time
from page_model.dresses_page import DressesPageLocators


class DressesPage(BaseSetup, WebDriverCustomClass):


    #def summer_dresses_image_click_on(self):
     #   self.hover_over_first_element_click_on_second(dressesButtonByXpath,
      #                                                home_page.get("dressesButtonActivateByXpath"), "xpath",
       #                                               home_page.get("dressesButtonCassualDressesByXpath"), "xpath")

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
