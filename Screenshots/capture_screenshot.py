import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
text=driver.find_element(By.XPATH,"//*[contains(text(),'OrangeHRM, Inc')]").click()
time.sleep(5)
current_window_id=driver.current_window_handle  ###gives us the id of current window
window_id=driver.window_handles  ###gives us the list of id of opened windows
driver.switch_to.window(current_window_id)
parentid=window_id[0]
childid=window_id[1]
driver.switch_to.window(parentid)
driver.switch_to.window(childid)
time.sleep(5)
# print(current_window_id)  ###C71303A5CBE8B326A9104965E95247DA
# print(window_id)  ###['73C7873AD5A17F3F87E348D923E586B1', '1AAA772D25261CDE9CFA8D9ECCAB0565']
text2=driver.find_element(By.XPATH,"//*[contains(text(),'Contact Sales')]").click()
time.sleep(5)