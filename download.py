import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": f"{os.getcwd()}\\downloads"}
chrome_options.add_experimental_option('prefs', prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(3)
driver.find_elements(By.XPATH, '//a')[6].click()
time.sleep(3)