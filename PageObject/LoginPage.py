from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    button = (By.ID, "login-button")
    hamburgerButton = (By.ID, "react-burger-menu-btn")
    logoutButton = (By.ID, "logout_sidebar_link")
    errorMsg = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enterUsername(self, username):
        # self.driver.find_element(By.ID, self.textBox_username_id).clear()
        # self.driver.find_element(By.ID, self.textBox_username_id).send_keys(username)
        self.clear(self.username)
        self.do_send_keys(self.username, username)

    def enterPassword(self, password):
        # self.driver.find_element(By.ID, self.textBox_password_id).clear()
        # self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)
        self.clear(self.password)
        self.do_send_keys(self.password, password)

    def clickLoginButton(self):
        # self.driver.find_element(By.ID, self.button_id).click()
        self.do_click(self.button)

    def logOut(self):
        # self.driver.find_element(By.ID, self.hamburgerButton_id).click()
        # self.driver.find_element(By.ID, self.logoutButton_id).click()
        self.do_click(self.hamburgerButton)
        self.do_click(self.logoutButton)

    def wrongDataError(self):
        errorMsg_element = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        return errorMsg_element.text


