from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


LOCATOR_GREEN_BUTTON = (By.ID, 'greenButton')


class HiddenLayersPage(MainPage):

    def green_button(self):
        try:
            self.find_element(LOCATOR_GREEN_BUTTON).click()
            return True
        except ElementClickInterceptedException:
            return False
