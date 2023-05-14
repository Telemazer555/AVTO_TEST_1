import time

import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


class BasePage:
    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield self.driver
        self.driver.quit()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    # def requests_response(self):
    #     self.driver.get(self.url)
    #     for request in self.driver.requests:
    #         if request.response:
    #             print(
    #                 request.url,
    #                 request.response.status_code,
    #                 request.response.headers['Content-Type']
    #             )

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


class TestRequestConnection:
    def test_request_connection(self, driver):
        piter_online = TestRequestConnectionPage(driver, "https://piter-online.net/")
        piter_online.open()

        piter_online.request_connection()
        time.sleep(3)


class RequestConnectionLocators:
    SELECT = (By.XPATH, '//div/div/div[1]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/a')
    Search = (By.XPATH, '//div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div')
    INPUT_ADDRESS = (By.XPATH,
                     '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input')
    INPUT_HOME = (By.XPATH,
                  '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input')
    INPUT_Connections = (By.XPATH,
                         '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/input')
    INPUT_apartments = (By.XPATH, '//html/body/div/div/div[8]/div[2]/div/div/div/ul/li[1]')
    INPUT_Rates = (By.XPATH, '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[3]/div')
    Cross = (
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/a')
    Plug = (
        By.XPATH,
        '//div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    NAME = (By.XPATH, '//div/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    NUMBER = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    OKS = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[5]/div')


class TestRequestConnectionPage(BasePage):
    locators = RequestConnectionLocators()

    def request_connection(self):
        self.go_to_element(self.element_is_present(self.locators.SELECT))
        time.sleep(1)
        self.element_is_visible(self.locators.Search).click()

        ADD_INPUT = self.element_is_visible(self.locators.INPUT_ADDRESS)
        ADD_INPUT.clear()
        ADD_INPUT.send_keys("Тестовая линия")
        time.sleep(1)
        ADD_INPUT.send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_is_visible(self.locators.INPUT_HOME).send_keys('1')
        time.sleep(1)

        self.element_is_visible(self.locators.INPUT_Connections).click()
        self.element_is_visible(self.locators.INPUT_apartments).click()
        self.element_is_visible(self.locators.INPUT_Rates).click()
        time.sleep(5)
        self.element_is_visible(self.locators.Cross).click()
        # time.sleep(25)
        # self.go_to_element(self.element_is_present(self.locators.Plug))
        self.element_is_visible(self.locators.Plug).click()
        # self.element_is_visible(self.locators.NAME).send_keys("Автотест")
        self.element_is_visible(self.locators.NUMBER).send_keys("1111111111")
        time.sleep(2)
        self.element_is_visible(self.locators.OKS).click()
        time.sleep(5)

        response = requests.post('https://orders.101internet.ru/api_external/sites/webhook?type=site101-order-home')
        request_headers = response.request.headers
        response_headers = response.headers
        response_text = response.text
        print(response)
        print(response_headers)
        print(request_headers)
        print("\nResponse text:\n", response_text)
