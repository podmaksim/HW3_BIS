from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


from pages.main_page import MainPage


LOCATOR_HIDING_BUTTON = (By.ID, 'hidingButton')


class ScrollbarsPage(MainPage):

    def hiding_button(self):
        try:
            self.driver.execute_script("arguments[0].click();", self.find_element(LOCATOR_HIDING_BUTTON))
            return True
        except TimeoutException:
            return False
