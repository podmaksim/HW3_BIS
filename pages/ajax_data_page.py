from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


LOCATOR_TRIGGERING_BUTTON = (By.ID, 'ajaxButton')
LOCATOR_TEXT = (By.XPATH, '//p[@class="bg-success"]')


class AjaxDataPage(MainPage):

    def triggering_button(self):
        self.find_element(LOCATOR_TRIGGERING_BUTTON).click()

    def wait_text(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(LOCATOR_TEXT))
            return True
        except TimeoutException:
            return False
