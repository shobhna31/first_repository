import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
