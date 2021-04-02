from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cnd

driver = webdriver.Chrome(executable_path="F:\Projects\chromedriver.exe")

driver.get("https://www.youtube.com/")

driver.implicitly_wait(3)
assert "YouTube" in driver.title

text_box = driver.find_element_by_name('search_query')
text_box.send_keys('Selenium')

driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon').click()

print(f'Title of Current Navigated page : {driver.title}')
print(f'URL of Current Navigated page : {driver.current_url}')

wait = WebDriverWait(driver, 10)
home = wait.until(exp_cnd.element_to_be_clickable((By.XPATH,"//*[@id='endpoint']")))
home.click()


print(f'Title of Current Navigated page : {driver.title}')
print(f'URL of Current Navigated page : {driver.current_url}')

driver.quit()
