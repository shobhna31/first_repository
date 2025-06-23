from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Login_page_object import LoginPage
from Pages.Forgot_password import ForgotPassword
class TestForgotPwd:
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
    driver.maximize_window()
    driver.implicitly_wait(10)
    lp=ForgotPassword(driver)
    lp.set_username("Admin")
    lp.reset_button()
    # actual_title=driver.title
    # expected_title="OrangeHRM"
    # assert actual_title==expected_title,"Test Failed"
    # print("Test Passed!")