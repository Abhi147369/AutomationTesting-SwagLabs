import pytest

from PageObject.CartPage import CartPage
from PageObject.LoginPage import LoginPage
from PageObject.ProductPage import ProductPage
from utilities.readProperties import ReadConfig


class Test__004_Cart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    checkoutInformationName = ReadConfig.checkoutInformationName()
    checkoutInformationLastName = ReadConfig.checkoutInformationLastName()
    checkoutInformationZipcode = ReadConfig.checkoutInformationZipcode()

    @pytest.mark.Regression
    @pytest.mark.Sanity
    def test_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        self.pp = ProductPage(self.driver)
        self.pp.backpack()
        self.pp.addToCart()
        self.pp.cart()

        self.cart = CartPage(self.driver)
        self.cart.checkout()
        self.driver.close()

    @pytest.mark.Regression
    @pytest.mark.Sanity
    def test_checkoutInformationName(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        self.pp = ProductPage(self.driver)
        self.pp.backpack()
        self.pp.addToCart()
        self.pp.cart()

        self.cart = CartPage(self.driver)
        self.cart.checkout()
        self.cart.checkoutInformationName(self.checkoutInformationName)
        self.cart.checkoutInformationLastName(self.checkoutInformationLastName)
        self.cart.checkoutInformationZipcode(self.checkoutInformationZipcode)

        self.cart.clickContinueButton()
        self.driver.close()
