import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl  ##
driver=webdriver.Chrome()
driver.find_element(By.ID, "fileUploadInput").send_keys(r"C:\Users\dell\Desktop\Shobhna-office\SDET\data-driven-testing-sheets\test.xlsx")
