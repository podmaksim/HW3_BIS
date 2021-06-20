from pages.base_page import BasePage
from selenium.webdriver.common.by import By


LOCATOR_DYNAMIC_ID_LINK = (By.XPATH, '//a[@href="/dynamicid"]')
LOCATOR_ClASS_ATTRIBUTE_LINK = (By.XPATH, '//a[@href="/classattr"]')
LOCATOR_HIDDEN_LAYERS_LINK = (By.XPATH, '//a[@href="/hiddenlayers"]')
LOCATOR_LOAD_DELAY_LINK = (By.XPATH, '//a[@href="/loaddelay"]')
LOCATOR_AJAX_DATA_LINK = (By.XPATH, '//a[@href="/ajax"]')
LOCATOR_CLIENT_SIDE_DELAY_LINK = (By.XPATH, '//a[@href="/clientdelay"]')
LOCATOR_CLICK_LINK = (By.XPATH, '//a[@href="/click"]')
LOCATOR_TEXT_INPUT_LINK = (By.XPATH, '//a[@href="/textinput"]')


class MainPage(BasePage):

    def dynamic_id_link(self):
        dynamic_link = self.find_element(LOCATOR_DYNAMIC_ID_LINK)
        dynamic_link.click()

    def class_attribute_link(self):
        class_attribute_link = self.find_element(LOCATOR_ClASS_ATTRIBUTE_LINK)
        class_attribute_link.click()

    def hidden_layers_link(self):
        hidden_layers_link = self.find_element(LOCATOR_HIDDEN_LAYERS_LINK)
        hidden_layers_link.click()

    def load_delay_link(self):
        load_delay_link = self.find_element(LOCATOR_LOAD_DELAY_LINK)
        load_delay_link.click()

    def ajax_data_link(self):
        ajax_data_link = self.find_element(LOCATOR_AJAX_DATA_LINK)
        ajax_data_link.click()

    def client_side_delay_link(self):
        client_side_delay_link = self.find_element(LOCATOR_CLIENT_SIDE_DELAY_LINK)
        client_side_delay_link.click()

    def click_link(self):
        click_link = self.find_element(LOCATOR_CLICK_LINK)
        click_link.click()

    def text_input_link(self):
        text_input_link = self.find_element(LOCATOR_TEXT_INPUT_LINK)
        text_input_link.click()
