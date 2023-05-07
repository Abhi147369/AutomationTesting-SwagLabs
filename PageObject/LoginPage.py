from selenium.webdriver.common.by import By


class LoginPage:
    textBox_username_id = "user-name"
    textBox_password_id = "password"
    button_id = "login-button"
    hamburgerButton_id = "react-burger-menu-btn"
    logoutButton_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element(By.ID, self.textBox_username_id).clear()
        self.driver.find_element(By.ID, self.textBox_username_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.textBox_password_id).clear()
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.button_id).click()

    def logOut(self):
        self.driver.find_element(By.ID, self.hamburgerButton_id).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.logoutButton_id).click()
