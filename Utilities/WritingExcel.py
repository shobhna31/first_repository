import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl  ##module for data driven testing



###File-->Workbook-->sheet-->rows-->cells(column)

# file=os.getcwd() + r"\test.xlsx"
file= r"C:\Users\dell\Desktop\Shobhna-office\SDET\data-driven-testing-sheets\test.xlsx"
workbook=openpyxl.load_workbook(file)
# sheet=workbook.active  ##or workbook["Sheet3"]
sheet=workbook["Sheet3"]

for r in range(1,6):
    for c in range(1,3):
        sheet.cell(r,c).value="Welcome"

workbook.save(file)
