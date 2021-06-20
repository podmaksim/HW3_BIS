from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


LOCATOR_TRIGGERING_SIDE_BUTTON = (By.ID, 'ajaxButton')
LOCATOR_TEXT = (By.XPATH, '//div[@id="content"]/p[@class="bg-success"]')


class ClientSidePage(MainPage):

    def triggering_side_button(self):
        self.find_element(LOCATOR_TRIGGERING_SIDE_BUTTON).click()

    def wait_text(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(LOCATOR_TEXT))
            return True
        except TimeoutException:
            return False
