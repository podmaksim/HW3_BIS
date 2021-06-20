from selenium.webdriver.common.by import By


from pages.main_page import MainPage


LOCATOR_INPUT_FIELD = (By.ID, 'newButtonName')
LOCATOR_CHANGE_BUTTON = (By.ID, 'updatingButton')

input_text = 'Padasep Maksim'


class TextInputPage(MainPage):

    def input_text(self):
        self.find_element(LOCATOR_INPUT_FIELD).send_keys(input_text)

    def click_change_button(self):
        self.find_element(LOCATOR_CHANGE_BUTTON).click()

    def check_button(self):
        new_text = self.find_element(LOCATOR_CHANGE_BUTTON).text
        assert input_text == new_text
