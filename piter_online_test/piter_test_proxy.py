import time

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import json


options = {
    'proxy': dict(http='http://localhost:8888', https='http://localhost:8888', no_proxy='http://localhost:8888')}
driver = webdriver.Chrome(seleniumwire_options=options)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
proxy_server_url = "http://localhost:8888"
options.add_argument(f'--proxy-server={proxy_server_url}')


# @pytest.fixture
def piter():
    testInputFIO = 'Автотест'
    testInputPhone = '1111111111'
    url = ('https://piter-online.net/')

    driver.maximize_window()
    driver.get(url)
    driver.execute_script("window.scrollBy(0.5,document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[text()= "Поиск по адресу"]').click()
    driver.find_element(By.XPATH, '//*[@id="fixed_navigation"]//div//span[text()= "Введите улицу"]').click()
    driver.find_element(By.XPATH,
                        '//*[@id="fixed_navigation"]/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys(
        'Тестовая линия')
    time.sleep(4)
    driver.find_element(By.XPATH,
                        '//*[@id="fixed_navigation"]/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys(
        Keys.ENTER)
    time.sleep(1)

    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input').send_keys(
        '1')
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//div/div/div[2]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/input').send_keys(
        Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="fixed_navigation"]//span[text()= "Тип подключения"]').click()
    driver.find_element(By.XPATH, '//*[@id="forSelectField"]/div[2]/div/div/div/ul/li[1]').click()
    driver.find_element(By.XPATH, '//*[@id="fixed_navigation"]//div[text()= "показать тарифы"]').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
    driver.find_element(By.XPATH, '//body/div/div/div[4]/div/div/div/div/div').click()
    # time.sleep(20)
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/a').click()
    time.sleep(2)

    # driver.find_element(By.XPATH,
    #                     '//div/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input').send_keys(
    #     testInputFIO)
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input').send_keys(
        testInputPhone)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[5]/div').click()
    # request = driver.wait_for_request('orders.101internet.ru/api_external/sites/webhook')
    # request = driver.wait_for_request('/api/sites/webhook?type=site101-order-home')
    # request = driver.wait_for_request('piter-online.net/api/sites/webhook?type=site101-order-home')
    request = driver.wait_for_request('https://piter-online.net/api/sites/webhook?type=site101-order-home')
    print("\nawaited response", request)

    if request.response.status_code == 200 and request.method == 'POST':
        requestBody = request.body.decode('utf-8')
        jsonDict = json.loads(requestBody)
        print("\n", requestBody, "\nfio: ", jsonDict['fio'], '\nphone: ', jsonDict['phone_connection'],
              type(jsonDict['fio']), type(testInputFIO))
        # if jsonDict['fio'] == testInputFIO and jsonDict['phone_connection'] == testInputPhone:
        if jsonDict['fio'] == testInputFIO and jsonDict['phone_connection'] == ("7" + testInputPhone):
            print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Ураааааа нахуй заработало")
        else:
            print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! Failure: запрос отработал успешно, но данные переданы некорректно")
    else:
        print("_!_!_!_!_!_!_!_!_!_!_!_!_!_! тест не пройден")


piter()
time.sleep(2)
driver.quit()
