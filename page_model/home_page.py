
class HomePageLocators:
    searchFieldByID = "search_query_top"
    searchButtonByName = "submit_search"
    cartButtonCSSSelector = "a b"
    dressesButtonByXpath = "(//a[@class='sf-with-ul'])[4]"
    dressesButtonActivateByXpath = "(//ul[@class='submenu-container clearfix first-in-line-xs'])[2]"
    dressesButtonCassualDressesByXpath = "(//a[@title='Summer Dresses'])[2]"
    womenButtonByXpath = "//a[@title='Women']"
    loginButtonByClassName = "header_user_info"
    emailRegisterInputTextByID = "email_create"
    registerButtonByID = "SubmitCreate"
    customerFirstNameInputTextByID = "customer_firstname"
    customerLastNameInputTextByID = "customer_lastname"
    genderMaleInputRadioByID = "id_gender1"
    passwordInputRadioByID = "passwd"
    stateSelectByID = "id_state"
    addressInputTextByID = "address1"
    cityInputTextByID = "city"
    zipcodeInputTextByID = "postcode"
    countrySelectByID = "id_country"
    phoneInputTextByID = "phone_mobile"
    aliasInputTextByID = "alias"
    submitRegisterButtonByID = "submitAccount"
    signInButtonByXpath = "//a[contains(text(),'Sign in')]"
    productNameLinkTextByXpath = "//a[contains(@class,'product-name')]"
    addCartButtonByID = "add_to_cart"
    checkoutButtonByXpath = "//span[contains(text(),'Proceed to checkout')]"
    productTitleLabelByXpath = "//h1[contains(@itemprop,'name')]"
    productQuantityLabelByID = "quantity_wanted"
    productPriceLabelByID = "our_price_display"


    '''
    keepShopButtonByXpath = "//span[contains(@title,'Continue shopping')]"
    closeAdd = PageElement(xpath='//*[@id="center_column"]/p[2]/a[1]')
    card = PageElement(xpath='//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    sumary = PageElement(xpath='//*[@id="center_column"]/p[2]/a[1]')
    confirmAddress = PageElement(name='processAddress')
    confirmShip = PageElement(name='processCarrier')
    termAgree = PageElement(id_='cgv')
    payByBank = PageElement(class_name='payment_module')
    confirmOrder = PageElement(xpath='//*[@id="cart_navigation"]/button')

    iconCart = PageElement(xpath='//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    close = PageElement(class_name='cross')
    '''