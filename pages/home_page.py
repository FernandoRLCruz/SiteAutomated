from random import randint

from selenium.webdriver.common.by import By

from base.base_setup import BaseSetup
from base.generic_methods import GenericMethodsClass
from page_model.home_page_model import HomePageLocators
from utilities.data import info_user, products_list
from base.product import Product


class HomePage(BaseSetup, GenericMethodsClass):
    product = Product
    product_dict = dict()

    def clickLoginButton(self):
        self.click_on_element(By.XPATH, HomePageLocators.signInButtonByXpath)

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
        self.fill_element(By.ID, HomePageLocators.passwordInputRadioByID, info_user['password'])
        self.fill_element(By.ID, HomePageLocators.addressInputTextByID, info_user['address'])
        self.fill_element(By.ID, HomePageLocators.cityInputTextByID, info_user['city'])
        self.selectOnCombo(By.ID, HomePageLocators.stateSelectByID, info_user['state'])
        self.fill_element(By.ID, HomePageLocators.zipcodeInputTextByID, info_user['zipcode'])
        self.selectOnCombo(By.ID, HomePageLocators.countrySelectByID, info_user['country'])
        self.fill_element(By.ID, HomePageLocators.phoneInputTextByID, info_user['phone'])
        self.fill_element(By.ID, HomePageLocators.aliasInputTextByID, info_user['email'])
        self.click_on_element(By.ID, HomePageLocators.submitRegisterButtonByID)

    def search_product(self, searched_product):
        self.send_keys_to(By.ID, HomePageLocators.searchFieldByID, searched_product)

    def search_button(self):
        self.click_on_element(By.NAME, HomePageLocators.searchButtonByName)

    def cart_button(self):
        self.click_on_element(By.CSS_SELECTOR, HomePageLocators.cartButtonCSSSelector)

    def dresses_button_click_on(self):
        self.click_on_element(By.XPATH, HomePageLocators.dressesButtonByXpath)

    def addInCart(self):
        for item in products_list['itens']:
            self.fill_element(By.ID, HomePageLocators.searchFieldByID, item)
            self.click_on_element(By.NAME, HomePageLocators.searchButtonByName)
            self.is_element_clickable(By.XPATH, HomePageLocators.productNameLinkTextByXpath)
            self.productElements = self.find_elements(By.XPATH, HomePageLocators.productNameLinkTextByXpath)
            self.productElement = self.findProductByName(item)
            self.productElement.click()
            self.is_element_clickable(By.ID, HomePageLocators.addCartButtonByID)
            self.product = self.getItemInCart()
            self.product_dict[self.product.name] = self.product
            self.click_on_element(By.ID, HomePageLocators.addCartButtonByID)
            self.is_element_clickable(By.XPATH, HomePageLocators.checkoutButtonByXpath)
            self.click_on_element(By.XPATH, HomePageLocators.checkoutButtonByXpath)
            self.cartValue = self.calculateCart()

    def registerAction(self):
        self.clickLoginButton()
        self.loadRegister()
        self.fillFormRegister()

    def getItemInCart(self):
        self.product.name = self.find_element(By.XPATH, HomePageLocators.productTitleLabelByXpath).text
        self.product.price = self.find_element(By.ID, HomePageLocators.productPriceLabelByID).text
        self.product.qtd = self.find_element(By.ID, HomePageLocators.productQuantityLabelByID).get_attribute("value")
        return self.product

    def findProductByName(self, item):
        for productItem in self.productElements:
            if item in productItem.text:
                return productItem

    def calculateCart(self):
        for productItem in self.product_dict:
            return int(self.product_dict[productItem].qtd) * int(self.product_dict[productItem].price[1:3])
