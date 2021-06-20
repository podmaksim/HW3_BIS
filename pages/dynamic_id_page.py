from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


LOCATOR_DYNAMIC_ID_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')


class DynamicIdPage(MainPage):

    def dynamic_id_button(self):
        try:
            self.find_element(LOCATOR_DYNAMIC_ID_BUTTON).click()
            return True
        except TimeoutException:
            return False
