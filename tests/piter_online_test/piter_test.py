import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import json

from pages.base_page import BasePage


class RequisitionForInternetPageInputData:
    testInputStreet = 'Тестовая линия'
    testInputHome = '1'
    testInputFIO = 'Автотест'
    testInputPhone = '1111111111'


class RequisitionForInternetLocators:
    SomeElementForTopBarAppearance = (By.XPATH, '//div/div/div[1]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/a')
    """Чтобы панель с кнопкой оформления заявки вверху страницы появилась, нужно немного проскролить страницу до этого элемента"""

    SearchButton = (By.CSS_SELECTOR, 'div [datatest="button_upper_compare_tariffs"]')
    AddressStreetTextField = (By.CSS_SELECTOR,
                              '[class="app141 app146 app143 app160 app142"]')
    AddressHomeNumberTextField = (By.CSS_SELECTOR,
                                  '[class="app141 app146 app143 app160"]')
    ConnectionTypesButton = (By.CSS_SELECTOR,
                             'div.app122 > div > div > div > div.app161 > input')
    ConnectionTypesListApartmentTypeElement = (By.XPATH, '//html/body/div/div/div[8]/div[2]/div/div/div/ul/li[1]')
    GoToTariffsButton = (By.XPATH,
                         '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[3]/div')
    PromoPopupCloseButton = (By.CSS_SELECTOR,
                             'div [datatest="close_popup1_from_quiz_input_tel"]')
    FirstTariffRequisitionButton = (By.XPATH,
                                    '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/a')
    Name = (By.XPATH, '//div/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
    PhoneNumberTextField = (By.XPATH,
                            '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input')


class RequisitionForInternetConnection(BasePage):
    """Проверка оформления заявки на проведение интернета в кваиртиру"""
    inputData = RequisitionForInternetPageInputData()
    locators = RequisitionForInternetLocators()

    def requisition(self):

        self.go_to_element(self.element_is_present(self.locators.SomeElementForTopBarAppearance))
        time.sleep(1)
        self.element_is_visible(self.locators.SearchButton).click()

        addressStreetField = self.element_is_visible(self.locators.AddressStreetTextField)
        addressStreetField.clear()
        addressStreetField.send_keys(self.inputData.testInputStreet)
        time.sleep(3)
        addressStreetField.send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_is_visible(self.locators.AddressHomeNumberTextField).send_keys(self.inputData.testInputHome)
        time.sleep(1)

        self.element_is_visible(self.locators.ConnectionTypesButton).click()
        self.element_is_visible(self.locators.ConnectionTypesListApartmentTypeElement).click()
        self.element_is_visible(self.locators.GoToTariffsButton).click()
        # Запрос при клике на INPUT_Rates часто меняется, из-за чего ожидание ответа на него не очень подходит, т.к. ломается тест. Используем sleep как универсальное решение
        time.sleep(5)
        self.element_is_visible(self.locators.PromoPopupCloseButton).click()
        time.sleep(1)
        self.element_is_visible(self.locators.FirstTariffRequisitionButton).click()
        self.element_is_visible(self.locators.PhoneNumberTextField).send_keys(self.inputData.testInputPhone)

        # Запрос /api/sites/webhook часто меняется
        request = self.driver.wait_for_request('/api/sites/webhook?type=site101-order-home')
        # print("\nawaited response", request)

        if request.response.status_code == 200 and request.method == 'POST':
            requestBody = request.body.decode('utf-8')
            jsonDict = json.loads(requestBody)
            # print("\n", requestBody, "\nfio: ", jsonDict['fio'], '\nphone: ', jsonDict['phone_connection'],
            #       type(jsonDict['fio']), type(self.inputData.testInputFIO))
            if jsonDict['fio'] == self.inputData.testInputFIO and jsonDict['phone_connection'] == (
                    "7" + self.inputData.testInputPhone):
                print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Тест пройден")
            else:
                print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Failure: запрос отработал успешно, но данные переданы некорректно")
        else:
            print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! тест не пройден")


class TestRequisitionForInternetConnectionRunner():

    def test_run(self, driver_wire):
        piter_online = RequisitionForInternetConnection(driver_wire, "https://piter-online.net/")
        # self.configure_charles_proxy(piter_online.driver)
        piter_online.open()
        piter_online.requisition()

    # def configure_charles_proxy(self, driver):
    #     print()
