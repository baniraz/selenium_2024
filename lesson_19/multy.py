import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument('--window-size=1920,1080')
user_1 = webdriver.Chrome(options=options)

LOGIN = (By.XPATH, '//input[@type="email"]')
PASSWORD = (By.XPATH, '//input[@type="password"]')
SUBMIT = (By.XPATH, '//button[@type="submit"]')

user_1.get('https://hyperskill.org/login')
user_1.find_element(*LOGIN).send_keys('alekseik@ya.ru')
user_1.find_element(*PASSWORD).send_keys('Qwerty132!')
user_1.find_element(*SUBMIT).click()
time.sleep(3)
user_1.close()

user_2 = webdriver.Chrome(options=options)
user_2.get('https://hyperskill.org/login')
time.sleep(3)