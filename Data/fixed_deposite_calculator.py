import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl  ##module for data driven testing
from selenium.webdriver.support.select import Select

import XLUtils
from basic_scripts.Data_driven_testing_using_Excel.XLUtils import getRowCount
driver=webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
file=r"C:\Users\dell\Desktop\Shobhna-office\SDET\data-driven-testing-sheets\caldata.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")
cols=XLUtils.getColumnCount(file,"Sheet1")
# print(rows)
# print(cols)

##Read data from Excel file
for r in range(2,rows+1):
    principle=XLUtils.readData(file,"Sheet1",r,1)
    rate_of_interest=XLUtils.readData(file,"Sheet1",r,2)
    period=XLUtils.readData(file,"Sheet1",r,3)
    days=XLUtils.readData(file,"Sheet1",r,4)
    frequency=XLUtils.readData(file,"Sheet1",r,5)
    expected_maturity_value=XLUtils.readData(file,"Sheet1",r,6)

##Pass sheet values to the input fields of the form

    prin=driver.find_element(By.ID,"principal").send_keys(principle)
    roi=driver.find_element(By.ID,"interest").send_keys(rate_of_interest)
    prd=driver.find_element(By.ID,"tenure").send_keys(period)
    no_of_days=Select(driver.find_element("name","tenurePeriod"))
    no_of_days.select_by_visible_text(days)
    freq = Select(driver.find_element("name", "frequency"))
    freq.select_by_visible_text(frequency)
    compute=driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img')
    # compute.click()
    ##use execute_script() method to overcome error:element click not intercepted
    driver.execute_script("arguments[0].click();",compute)
    act_maturity_value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    time.sleep(4)

    if float(expected_maturity_value)==float(act_maturity_value):
        print("Test Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    clear_btn=driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img')
    driver.execute_script("arguments[0].click()",clear_btn)