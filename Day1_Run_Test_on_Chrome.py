from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="F:\Projects\chromedriver.exe")
driver.get("https://www.youtube.com/")

print(driver.title)
print(driver.current_url)
driver.close()