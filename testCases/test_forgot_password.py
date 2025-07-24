from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    wait=WebDriverWait(driver,10)
    success_message = wait.until(EC.presence_of_element_located((By.TAG_NAME,"h6"))).text
    assert "Reset Password link sent successfully" in success_message,"Test Failed!!!"
    print("Test Passed!!!")
    driver.quit()



