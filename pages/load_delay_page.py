from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


from pages.main_page import MainPage


LOCATOR_AFTER_DELAY_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')


class AfterDelayPage(MainPage):

    def after_delay_button(self):
        try:
            self.find_element(LOCATOR_AFTER_DELAY_BUTTON).click()
            return True
        except ElementClickInterceptedException:
            return False
