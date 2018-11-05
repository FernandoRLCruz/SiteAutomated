from selenium.webdriver.common.by import By
from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from page_model.home_page_logado_model import HomeLogadoPageLocators
from utilities.data import info_user


class HomeLogadoPage(BaseSetup, GenericMethodsClass):

    def getTextLabel(self):
        element = self.find_element(By.XPATH, HomeLogadoPageLocators.titleLoggedH1ByXpath)
        return element.text

