from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from page_model.login_page_model import LoginPageLocators
from utilities.data import info_user_logged


class LoginPage(BaseSetup, WebDriverCustomClass):

    def fillLogin(self):
        self.is_element_clickable(By.ID, LoginPageLocators.emailRegisterInputTextByID)
        self.fill_element(By.ID, LoginPageLocators.loginMailInputTextByID, info_user_logged['email'])
        self.fill_element(By.ID, LoginPageLocators.loginPassInputTextByID, info_user_logged['password'])

    def clickLogin(self):
        self.click_on_element(By.ID, LoginPageLocators.loginButtonByID)

    def loginSuccessful(self):
        self.fillLogin()
        self.clickLogin()
