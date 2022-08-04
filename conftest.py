# coding: utf8
import pytest
from settings import *
from appium import webdriver


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    global driver
    capabilities = {
        'platformName': (CONFIG[platform]['platformName']),
        'platformVersion': (CONFIG[platform]['platformVersion']),
        'deviceName': (CONFIG[platform]['deviceName']),
        'automationName': (CONFIG[platform]['automationName']),
        'appPackage': (CONFIG[platform]['appPackage']),
        'appActivity': (CONFIG[platform]['appActivity']),
        'noReset': (CONFIG[platform]['noReset']),
        'app': (CONFIG[platform]['folder']),
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

    def teardown():
        driver.quit()
    request.addfinalizer(teardown)
