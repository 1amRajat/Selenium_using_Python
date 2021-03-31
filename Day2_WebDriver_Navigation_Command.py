from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\Projects\chromedriver.exe")

driver.get("https://www.youtube.com/")
time.sleep(3)
print(driver.title)

driver.get("https://www.google.com/")
time.sleep(3)
print(driver.title)

driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)

driver.quit()