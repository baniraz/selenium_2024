import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/alerts')

BUTTON_1 = (By.XPATH, '//button[@id="alertButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.accept()
time.sleep(3)

BUTTON_3 = (By.XPATH, '//button[@id="confirmButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
print(alert.text)
alert.dismiss()
time.sleep(3)

BUTTON_4 = (By.XPATH, '//button[@id="promtButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.send_keys('Test')
time.sleep(3)
alert.accept()
time.sleep(3)