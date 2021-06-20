from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

