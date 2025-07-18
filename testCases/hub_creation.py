from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

GRID_URL="http://172.20.10.3:4444"
##desired capabilities
options=webdriver.ChromeOptions()
options.set_capability("browserName","chrome")
options.set_capability("platformName","WINDOWS")
driver=webdriver.Remote(command_executor=GRID_URL, options=options)
driver.get("https://www.google.com/")
print("Page Title: ",driver.title)

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium grid with python")
search_box.send_keys(Keys.RETURN)
# search_box.submit()


#connecting node with remote hub
# java -jar selenium-server-4.33.0.jar node --hub http://192.168.1.175:4444