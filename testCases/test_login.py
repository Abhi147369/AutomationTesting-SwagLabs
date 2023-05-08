from PageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test__01__Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        if title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title Is Passed **********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title Is Failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("********** Login Test Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("********** Login Test Passed **********")
        self.driver.close()

    def test_logout(self, setup):
        self.logger.info("********** Logout Test Started **********")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        self.lp.logOut()
        self.logger.info("********** Logout Test Passed **********")
        self.driver.close()
