import time

import pytest
import pytest_html
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
@allure.feature("OrangeHRM Forgot/Reset Password")
@allure.story("Reset Password Success Page")
@allure.severity(allure.severity_level.CRITICAL)
class LoginPage:
    ##Element Locators
    txt_username_name="username"
    txt_pwd_name="password"
    btn_login="//*[@class='oxd-form-actions orangehrm-login-action']/button"

    ##initiate driver
    def __init__(self,driver):
        self.driver=driver

    ##Actions
    def set_username(self,username):    
        uname=self.driver.find_element(By.NAME,self.txt_username_name)
        uname.send_keys(username)

    def set_password(self,password):
        passwd=self.driver.find_element(By.NAME,self.txt_pwd_name)
        passwd.send_keys(password)
    def click_button(self):
        login=self.driver.find_element(By.XPATH,self.btn_login)
        login.click()


    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        outcome = yield
        report = outcome.get_result()
        if report.failed:
            driver = item.funcargs['driver']
            screenshot = driver.get_screenshot_as_base64()
            report.extra = getattr(report, 'extra', [])
            report.extra.append(pytest_html.extras.image(screenshot, mime_type='image/png'))


    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

