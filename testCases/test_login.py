from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Login_page_object import LoginPage
from logger_utils import get_logger

logger = get_logger()
class TestLogin:
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # base_url=""
    # driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    lp=LoginPage(driver)
    lp.set_username("Admin")
    lp.set_password("admin123")
    lp.click_button()
    actual_title=driver.title
    expected_title="OrangeHRM"
    assert actual_title==expected_title,"Test Failed"
    print("Test Passed!")
    driver.quit()

