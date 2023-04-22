import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json


class MainPage:
    def __init__(self, driver_wire, url):
        self.driver = driver_wire
        self.url = url

    def open(self):
        self.driver.get(self.url)

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


class PageLiterals:
    testInputStreet = 'Тестовая линия'
    testInputHome = '1'
    testInputFIO = 'Автотест'
    testInputPhone = '1111111111'


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
    Cross = (By.XPATH, '//body/div/div/div[4]/div/div/div/div/div')
    Plug = (
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/a')
    NAME = (By.XPATH, '//div/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    NUMBER = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    OKS = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[5]/div')


class Perexvat(MainPage):
    Literals = PageLiterals()
    locators = RequestConnectionLocators()

    def piter(self):

        self.go_to_element(self.element_is_present(self.locators.SELECT))
        time.sleep(1)
        self.element_is_visible(self.locators.Search).click()

        ADD_INPUT = self.element_is_visible(self.locators.INPUT_ADDRESS)
        ADD_INPUT.clear()
        ADD_INPUT.send_keys(self.Literals.testInputStreet)
        time.sleep(3)
        ADD_INPUT.send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_is_visible(self.locators.INPUT_HOME).send_keys(self.Literals.testInputHome)
        time.sleep(1)

        self.element_is_visible(self.locators.INPUT_Connections).click()
        self.element_is_visible(self.locators.INPUT_apartments).click()
        self.element_is_visible(self.locators.INPUT_Rates).click()
        time.sleep(5)
        self.element_is_visible(self.locators.Cross).click()
        # time.sleep(25)
        self.go_to_element(self.element_is_present(self.locators.Plug))
        self.element_is_visible(self.locators.Plug).click()
        # self.element_is_visible(self.locators.NAME).send_keys(self.Literals.testInputFIO)
        self.element_is_visible(self.locators.NUMBER).send_keys(self.Literals.testInputPhone)
        # time.sleep(2)
        # self.element_is_visible(self.locators.OKS).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,
        #                          '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[5]/div').click()
        time.sleep(2)
        request = self.driver.wait_for_request('/api/sites/webhook?type=site101-order-home')
        # request = self.driver.wait_for_request('https://piter-online.net/api/sites/webhook?type=site101-order-home')
        # request = self.driver.wait_for_request('https://piter-online.net/api/sites/webhook?type=site101-order-home')


        print("\nawaited response", request)

        if request.response.status_code == 200 and request.method == 'POST':
            requestBody = request.body.decode('utf-8')
            jsonDict = json.loads(requestBody)
            print("\n", requestBody, "\nfio: ", jsonDict['fio'], '\nphone: ', jsonDict['phone_connection'],
                  type(jsonDict['fio']), type(self.Literals.testInputFIO))
            # if jsonDict['fio'] == testInputFIO and jsonDict['phone_connection'] == testInputPhone:
            if jsonDict['fio'] == self.Literals.testInputFIO and jsonDict['phone_connection'] == (
                    "7" + self.Literals.testInputPhone):
                print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Ураааааа нахуй заработало")
            else:
                print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Failure: запрос отработал успешно, но данные переданы некорректно")
        else:
            print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! тест не пройден")
            print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! тест не пройден")


class TestAvto():

    def test_avto(self, driver_wire):
        piter_online = Perexvat(driver_wire, "https://piter-online.net/")
        piter_online.open()
        piter_online.piter()
