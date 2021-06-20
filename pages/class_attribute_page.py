from selenium.common.exceptions import TimeoutException

from pages.main_page import MainPage
from selenium.webdriver.common.by import By


LOCATOR_BLUE_BUTTON = (By.CLASS_NAME, 'btn-primary')


class ClassAttributePage(MainPage):

    def blue_button(self):
        try:
            self.find_element(LOCATOR_BLUE_BUTTON).click()
            return True
        except TimeoutException:
            return False
