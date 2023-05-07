import time

from selenium.webdriver.common.by import By


class CartPage:
    continue_shopping_id = "continue-shopping"
    checkout_xpath = "//button[@id='checkout']"
    checkout_information_name_id = "first-name"
    checkout_information_last_name_id = "last-name"
    checkout_information_zipcode_id = "postal-code"
    continue_button_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.XPATH, self.checkout_xpath).click()

    def checkoutInformationName(self, checkoutInformationName):
        self.driver.find_element(By.ID, self.checkout_information_name_id).clear()
        self.driver.find_element(By.ID, self.checkout_information_name_id).send_keys(checkoutInformationName)

    def checkoutInformationLastName(self, checkoutInformationLastName):
        self.driver.find_element(By.ID, self.checkout_information_last_name_id).clear()
        self.driver.find_element(By.ID, self.checkout_information_last_name_id).send_keys(checkoutInformationLastName)

    def checkoutInformationZipcode(self, checkoutInformationZipcode):
        self.driver.find_element(By.ID, self.checkout_information_zipcode_id).clear()
        self.driver.find_element(By.ID, self.checkout_information_zipcode_id).send_keys(checkoutInformationZipcode)

    def clickContinueButton(self):
        self.driver.find_element(By.ID, self.continue_button_id).click()
