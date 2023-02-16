#import time

#from pages.base_page import BasePage


#def test(driver):
    #page = BasePage(driver, 'https://www.google.kz/')
    #page.open()
    #time.sleep(3)
#####################
#class BasePage:
    #def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    #def open(self):
        self.driver.get(self.url)
####################

import pytest
#from selenium import webdriver
#import webdriver_manager.chrome


#@pytest.fixture(scope='functon')
#def driver():
    #driver = webdriver.Chrome(webdriver_manager.ChromeDriverManager().install())
    #driver.maximize_window()
    #yield driver
    #driver.quit()
#########


