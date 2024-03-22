import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get('https://demoqa.com/upload-download')
time.sleep(3)
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f'{os.getcwd()}\\downloads\\download (1).jpg')
time.sleep(3)


# driver.get('https://the-internet.herokuapp.com/upload')
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f'{os.getcwd()}\\downloads\\download (1).jpg')
# time.sleep(3)