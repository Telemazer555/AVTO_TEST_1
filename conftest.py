import pytest
from selenium import webdriver as seldriver
from seleniumwire import webdriver as wiredriver


@pytest.fixture(scope='function')
def driver_wire():
    driver = wiredriver.Chrome()
    driver.maximize_window()
    # options = wiredriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # driver = wiredriver.Chrome(options=options)
    # driver = wiredriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver():
    driver = seldriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
