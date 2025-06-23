import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class ForgotPassword:
    ##Element Locators
    txt_username_name="username"
    btn_reset="//*[@class='orangehrm-forgot-password-button-container']/button[2]"

    ##initiate driver
    def __init__(self,driver):
        self.driver=driver

    ##Actions
    def set_username(self,username):
        uname = self.driver.find_element(By.NAME, self.txt_username_name)
        uname.send_keys(username)
    def reset_button(self):
        reset=self.driver.find_element(By.XPATH,self.btn_reset)
        reset.click()