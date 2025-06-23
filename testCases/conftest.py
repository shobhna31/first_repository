import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.find_element(By.NAME, "email").send_keys("shobhna.shrma@gmail.com")
        driver.find_element(By.NAME, "passwd").send_keys("shobhna@123")
        driver.find_element(By.NAME, "SubmitLogin").click()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser=="edge":
        driver=webdriver.Edge()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.find_element(By.NAME, "email").send_keys("shobhna.shrma@gmail.com")
        driver.find_element(By.NAME, "passwd").send_keys("shobhna@123")
        driver.find_element(By.NAME, "SubmitLogin").click()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Firefox()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.find_element(By.NAME, "email").send_keys("shobhna.shrma@gmail.com")
        driver.find_element(By.NAME, "passwd").send_keys("shobhna@123")
        driver.find_element(By.NAME, "SubmitLogin").click()
        driver.implicitly_wait(10)
        driver.maximize_window()


def pytest_addoption(parser):
    parser.addoption("--browser" )  ##this will get the value from command line prompt


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

##adding hooks to generate the html reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
