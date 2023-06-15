

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clear(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    def do_click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title
