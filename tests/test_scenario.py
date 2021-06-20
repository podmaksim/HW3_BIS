from pages.main_page import MainPage
from pages.dynamic_id_page import DynamicIdPage
from pages.class_attribute_page import ClassAttributePage
from pages.hidden_layers_page import HiddenLayersPage
from pages.load_delay_page import AfterDelayPage
from pages.ajax_data_page import AjaxDataPage
from pages.client_side_delay_page import ClientSidePage
from pages.click_page import ClickPage
from pages.text_input_page import TextInputPage


def test_dynamic_id(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.dynamic_id_link()
    dynamic_id_page = DynamicIdPage(browser)
    dynamic_id_page.dynamic_id_button()


def test_class_attribute(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.class_attribute_link()
    class_attribute_page = ClassAttributePage(browser)
    class_attribute_page.blue_button()


def test_hidden_layers(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.hidden_layers_link()
    hidden_layer_page = HiddenLayersPage(browser)
    hidden_layer_page.green_button()
    hidden_layer_page.green_button()


def test_delay(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.load_delay_link()
    after_delay_page = AfterDelayPage(browser)
    after_delay_page.after_delay_button()


def test_ajax_data(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.ajax_data_link()
    ajax_data_page = AjaxDataPage(browser)
    ajax_data_page.triggering_button()
    ajax_data_page.wait_text()


def test_client_side(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.client_side_delay_link()
    client_side_page = ClientSidePage(browser)
    client_side_page.triggering_side_button()
    client_side_page.wait_text()


def test_click(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.click_link()
    click_page = ClickPage(browser)
    click_page.ignore_button()
    click_page.green_button()


def test_text_input(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.text_input_link()
    text_input_page = TextInputPage(browser)
    text_input_page.input_text()
    text_input_page.click_change_button()
    text_input_page.check_button()
