from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


from pages.main_page import MainPage


LOCATOR_IGNORE_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
LOCATOR_GREEN_BUTTON = (By.XPATH, '//button[@class="btn btn-success"]')


class ClickPage(MainPage):

    def ignore_button(self):
        self.find_element(LOCATOR_IGNORE_BUTTON).click()

    def green_button(self):
        try:
            self.find_element(LOCATOR_GREEN_BUTTON)
            return True
        except TimeoutException:
            return False
