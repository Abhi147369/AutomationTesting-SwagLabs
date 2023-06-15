import pytest

from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test__01__Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    wrongUsername = ReadConfig.wrongUsername()
    wrongPassword = ReadConfig.wrongPassword()

    @pytest.mark.Regression
    def test_homepageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        if title == "Swag Labs":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        self.driver.close()

    def test_wrongDataLogin(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.wrongUsername)
        self.lp.enterPassword(self.wrongPassword)
        self.lp.clickLoginButton()
        errMsg = self.lp.wrongDataError()  # Call the method to retrieve the error message
        actualErrMsg = "Epic sadface: Username and password do not match any user in this service"

        print(errMsg)
        print(actualErrMsg)

        if errMsg == actualErrMsg:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_errorMsg.png")
            self.driver.close()
            assert False
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        self.lp.logOut()
        self.driver.close()
