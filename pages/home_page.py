import time
from random import randint

from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from page_model.home_page import HomePageLocators
from utilities.data import info_user


class HomePage(BaseSetup, WebDriverCustomClass):

    def clickLoginButton(self):
        self.click_on_element(By.CLASS_NAME, HomePageLocators.loginButtonByClassName)

    def loadRegister(self):
        self.is_element_clickable(By.ID, HomePageLocators.emailRegisterInputTextByID)
        self.fill_element(By.ID, HomePageLocators.emailRegisterInputTextByID, info_user['email'] + str(randint(0, 9)))
        self.is_element_clickable(By.ID, HomePageLocators.emailRegisterInputTextByID)
        self.click_on_element(By.ID, HomePageLocators.registerButtonByID)

    def fillFormRegister(self):
        self.is_element_clickable(By.ID, HomePageLocators.genderMaleInputRadioByID)
        self.click_on_element(By.ID, HomePageLocators.genderMaleInputRadioByID)
        self.fill_element(By.ID, HomePageLocators.customerFirstNameInputTextByID, info_user['firstName'])
        self.fill_element(By.ID, HomePageLocators.customerLastNameInputTextByID, info_user['lastName'])
        self.fill_element(self.password, info_user['password'])
        assert info_user['firstName'] in self.fName.get_attribute('value')
        assert info_user['lastName'] in self.lName.get_attribute('value')
        fillelement(self.address, info_user['address'])
        fillelement(self.city, info_user['city'])
        selectOnCombo(self.state, info_user['state'])
        fillelement(self.zipcode, info_user['zipcode'])
        selectOnCombo(self.country, info_user['country'])
        fillelement(self.phone, info_user['phone'])
        fillelement(self.alias, info_user['email'])
        self.submitAcc.click()


    def search_product(self, searched_product):
        self.send_keys_to(By.ID, HomePageLocators.searchFieldByID, searched_product)

    def search_button(self):
        self.click_on_element(By.NAME, HomePageLocators.searchButtonByName)

    def cart_button(self):
        self.click_on_element(By.CSS_SELECTOR, HomePageLocators.cartButtonCSSSelector)

    def dresses_button_click_on(self):
        self.click_on_element(By.XPATH, HomePageLocators.dressesButtonByXpath)

    def dresses_summer_dresses_click_on(self):
        pass

    def registerAction(self):
        self.clickLoginButton()
        self.loadRegister()
