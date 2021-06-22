import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestDynamicId(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_dynamic_id_button(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/dynamicid"]').click()
        self.assertIsNone(self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click())

    def tearDown(self):
        self.driver.close()


class TestClassAttribute(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_class_attribute(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/classattr"]').click()
        self.assertIsNone(self.driver.find_element(By.CLASS_NAME, 'btn-primary').click())

    def tearDown(self):
        self.driver.quit()


class TestHiddenLayers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_hidden_layers(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/hiddenlayers"]').click()
        self.assertIsNone(self.driver.find_element(By.ID, 'greenButton').click())

    def tearDown(self):
        self.driver.quit()


class TestLoadDelay(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_load_delay(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/loaddelay"]').click()
        self.assertIsNone(WebDriverWait(self.driver, 16).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))).click())

    def tearDown(self):
        self.driver.quit()


class TestAjaxData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_ajax_data(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/ajax"]').click()
        self.driver.find_element(By.ID, 'ajaxButton').click()
        self.assertIsNotNone(WebDriverWait(self.driver, 16).until(EC.presence_of_element_located((
            By.XPATH, '//p[@class="bg-success"]'))))

    def tearDown(self):
        self.driver.quit()


class TestClientSideDelay(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_client_side_delay(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/clientdelay"]').click()
        self.driver.find_element(By.ID, 'ajaxButton').click()
        self.assertIsNotNone(WebDriverWait(self.driver, 16).until(EC.presence_of_element_located((
            By.XPATH, '//div[@id="content"]/p[@class="bg-success"]'))))

    def tearDown(self):
        self.driver.quit()


class TestClick(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/click"]').click()
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.assertIsNone(self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click())

    def tearDown(self):
        self.driver.quit()


class TestTextInput(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_text_input(self):
        input_text = 'Padasep Maksim'
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/textinput"]').click()
        self.driver.find_element(By.ID, 'newButtonName').send_keys(input_text)
        self.driver.find_element(By.ID, 'updatingButton').click()
        self.assertEqual(self.driver.find_element(By.ID, 'updatingButton').text, input_text)

    def tearDown(self):
        self.driver.close()


class TestScrollbars(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_scrollbars(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/scrollbars"]').click()
        self.assertIsNone(self.driver.find_element(By.XPATH, '//button[contains(text(), "Hiding Button")]').click())

    def tearDown(self):
        self.driver.quit()


class TestDynamicTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_dynamic_table(self):
        driver = self.driver
        driver.get("http://www.uitestingplayground.com//")
        self.driver.find_element(By.XPATH, '//a[@href="/dynamictable"]').click()
        value_1 = self.driver.find_element(By.XPATH,
                                 '//div[@role="row"]//span[contains( text(),"Chrome")]'
                                 '//following::span[contains( text(),"%")][1]').text
        value_2 = self.driver.find_element(By.XPATH, '//p[@class="bg-warning"]').text
        self.assertIn(value_1, value_2)

    def tearDown(self):
        self.driver.close()
