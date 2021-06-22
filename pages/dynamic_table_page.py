from selenium.webdriver.common.by import By
from pages.main_page import MainPage


LOCATOR_CHROME_CPU_BUTTON = (By.XPATH,
                             '//div[@role="row"]//span[contains( text(),"Chrome")]//following::span[contains( text(),"%")][1]')
LOCATOR_CHROME_CPU_TEST_BUTTON = (By.XPATH, '//p[@class="bg-warning"]')


class DynamicTablePage(MainPage):

    def check_cpu(self):
        value_1 = self.find_element(LOCATOR_CHROME_CPU_BUTTON).text
        value_2 = self.find_element(LOCATOR_CHROME_CPU_TEST_BUTTON).text

        assert value_1 in value_2
