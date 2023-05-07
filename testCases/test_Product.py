import time

from PageObject.LoginPage import LoginPage
from PageObject.ProductPage import ProductPage
from utilities.readProperties import ReadConfig


class Test__003_Product:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_backpack(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        self.pp = ProductPage(self.driver)
        self.pp.backpack()
        self.driver.close()

    def test_add_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        self.pp = ProductPage(self.driver)
        self.pp.backpack()
        self.pp.addToCart()
        self.driver.close()

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
        self.driver.close()
