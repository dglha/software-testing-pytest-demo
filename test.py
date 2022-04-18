from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.python.org")
