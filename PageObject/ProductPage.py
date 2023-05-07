from selenium.webdriver.common.by import By


class ProductPage:
    backpack_id = "item_4_title_link"
    add_to_cart_id = "add-to-cart-sauce-labs-backpack"
    cart_xpath = "//a[@class='shopping_cart_link']"

    def __init__(self, driver):
        self.driver = driver

    def backpack(self):
        self.driver.find_element(By.ID, self.backpack_id).click()

    def addToCart(self):
        self.driver.find_element(By.ID, self.add_to_cart_id).click()

    def cart(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()