import pytest

from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test__01__Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

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
