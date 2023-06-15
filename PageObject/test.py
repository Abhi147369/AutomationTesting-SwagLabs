from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def wrongDataError(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("1212")
    driver.find_element(By.ID, "password").send_keys("121")
    driver.find_element(By.ID, "login-button").click()

    errorMsg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    return errorMsg

def err():
    errmsg = "Epic sadface: Username and password do not match any user in this service"
    actual_error = wrongDataError(driver)  # Call the function and store its result
    if actual_error == errmsg:
        assert True
    else:
        assert False

wrongDataError(driver)
err()
