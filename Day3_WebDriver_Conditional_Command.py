from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\Projects\chromedriver.exe")

driver.get("https://www.youtube.com/")
print(f'Current title of the launched page is {driver.title}')

text_box = driver.find_element_by_name('search_query')

print(f'The text box display : {text_box.is_displayed()}')
print(f'The text box enable : {text_box.is_enabled()}')

text_box.send_keys('Selenium')
print(f'The text box selected : {text_box.is_selected()}') #since there is not radio button or check box, this will return false

driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon').click()
time.sleep(5)

print(f'Title of Current Navigated page : {driver.title}')
print(f'URL of Current Navigated page : {driver.current_url}')

driver.quit()
