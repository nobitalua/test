import webbrowser

import pytest
from selenium import webdriver
import time
driver = None

#scope: co nghia la chi chay 1 lan trongp ham vi class, ko can phai lap di lap lai cho tat ca cac lan chay
#vi du:
#test_fixtureDemo.py::TestExample::test_fixtureDemo1 do it first
#test_fixtureDemo.py::TestExample::test_fixtureDemo2 PASSED
#test_fixtureDemo.py::TestExample::test_fixtureDemo4 PASSED
#do it last

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path ="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="C:/Users/Vi PHAM/AppData/Local/Programs/Python/Python310/Scripts/geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://google.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def setup():
    print("do it first")
    yield
    print("do it last ")


@pytest.fixture()
def dataload():
    print("day la du lieu de chay")
    return ["phan tu 1","phan tu 2","phan tu 3"]


@pytest.fixture(params=[("chrome", "phan tu 1", "phan tu 2"), ("firefox","phan tu 3"), ("IE","SA")])
def crossBrowser(request):
    return request.param

