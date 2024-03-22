import os
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get('https://demoqa.com/dynamic-properties')
# #VISIBLE_AFTER_BUTTON = (By.XPATH, '//button[@id="visibleAfter"]')
# ENABLE_IN_SECONDS = (By.XPATH, '//button[@id="enableAfter"]')
# #BUTTON = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
# BUTTON = wait.until(EC.visibility_of_element_located(ENABLE_IN_SECONDS))
# BUTTON.click()
#
# driver.get('https://the-internet.herokuapp.com/dynamic_controls')
# REMOVE_BUTTON = (By.XPATH, '//button[text()="Remove"]')
# driver.find_element(*REMOVE_BUTTON).click()
# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
#
# driver.get('https://the-internet.herokuapp.com/dynamic_controls')
# ENABLE_BUTTON = (By.XPATH, '//button[text()="Enable"]')
# TEXT_FIELD = (By.XPATH, '//input[@type="text"]')
# wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
# wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Hello')
# wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello'))
# print('Ok')

driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
CHANGE_TEXT_TO_SW = (By.XPATH, '//button[@id="populate-text"]')
driver.find_element(*CHANGE_TEXT_TO_SW).click()
TEXT_FIELD = (By.XPATH, '//h2[@id="h2"]')
wait.until(EC.text_to_be_present_in_element(TEXT_FIELD, 'Selenium Webdriver'))
print('Ok')
DISPLAY_BUTTON = (By.XPATH, '//button[@id="display-other-button"]')
driver.find_element(*DISPLAY_BUTTON).click()
ENABLED = (By.XPATH, '//button[@id="hidden"]')
wait.until(EC.visibility_of_element_located(ENABLED))
print('Ok')
ENABLE_BUTTON = (By.XPATH, '//button[@id="enable-button"]')
driver.find_element(*ENABLE_BUTTON).click()
BUTTON = (By.XPATH, '//button[@id="disable"]')
wait.until(EC.element_to_be_clickable(BUTTON)).click()
print('Ok')
CLICK_BUTTON = (By.XPATH, '//button[@id="alert"]')
driver.find_element(*CLICK_BUTTON).click()
BUTTON = (By.XPATH, '//button[@id="disable"]')
wait.until(EC.alert_is_present())
print('Ok')