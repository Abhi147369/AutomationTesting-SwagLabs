from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def setup(browser, request):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")


############# Pytest HTML Report ##################

def pytest_configure(config):
    config._metadata['Project Name'] = 'SwagLabs'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abhishek Gavkare'
