import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.CLASS_NAME, 'wikipedia-icon')
driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
time.sleep(5)

# driver.get('https://hyperskill.org/tracks')
#print(len(driver.find_elements(By.CLASS_NAME, 'nav-link')))
# time.sleep(5)
# driver.find_elements(By.CLASS_NAME, 'nav-link')[0].click()
# time.sleep(5)

