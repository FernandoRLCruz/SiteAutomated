class OrderPageLocators:
    proceedCheckoutSummaryButtonByXpath = \
        "//p[contains(@class,'cart_navigation clearfix')]//a[contains(@title,'Proceed to checkout')]"
    proceedCheckoutAddressButtonByName = "processAddress"
    termsServiceCheckoutAddressButtonByID = "cgv"
    proceedCheckoutShippingButtonByName = "processCarrier"
    payByBankCheckoutPaymentByXpath = "//a[contains(@title,'Pay by bank wire')]"
    confirmOrderButtonByXpath = "//span[contains(text(), 'I confirm my order')]"
    orderConfirmLabelByXpath = "//strong[contains(text(),'Your order on My Store is complete.')]"
    priceFinalOrderLabelByXpath = "//span[contains(@class,'price')]//strong"
    shippingCheckoutLabelByID = "total_shipping"
