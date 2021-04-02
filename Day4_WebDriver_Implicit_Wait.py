from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\Projects\chromedriver.exe")

driver.get("https://www.youtube.com/")

driver.implicitly_wait(10)
assert "YouTube" in driver.title


text_box = driver.find_element_by_name('search_query')
text_box.send_keys('Selenium')

driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon').click()
time.sleep(2)

print(f'Title of Current Navigated page : {driver.title}')
print(f'URL of Current Navigated page : {driver.current_url}')

driver.quit()
