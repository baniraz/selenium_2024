import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get('https://freeconferencecall.com/global/pl')
#
# login_button = driver.find_element(By.XPATH, '//a[@id="login-desktop"]')
# login_button.click()
#
# email_field = driver.find_element(By.XPATH, '//input[@id="login_email"]')
# email_field.send_keys('test1@mail.ru')
#
# print(email_field.get_attribute('value'))
# print(email_field.get_attribute('maxlength'))
#
# email_field.clear()
#
# email_field.send_keys('test1111111@mail.ru')
# time.sleep(3)
#
# email_field.clear()
# email_field = driver.find_element(By.XPATH, '//input[@id="login_email"]')
# assert email_field.get_attribute("value") == ""
# email_field.send_keys('test22222@mail.ru')
# time.sleep(3)
# email_field_value = email_field.get_attribute("value")
# assert 'test22222@mail.ru' in email_field_value
#
#
# MY_LINK = driver.find_element("xpath", "//a[text()='Study plan']")
#
# print(MY_LINK.get_attribute("href"))
# print(MY_LINK.get_attribute("class"))
# print(MY_LINK.get_attribute("target"))
# print(MY_LINK.get_attribute("data-component-name"))

# driver.get('https://demoqa.com/text-box')
# full_name = driver.find_element(By.XPATH, '//input[@id="userName"]')
# full_name.clear()
# full_name.send_keys('Test01')
# full_name_value = full_name.get_attribute('value')
# assert 'Test01' in full_name_value
#
# email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
# email.clear()
# email.send_keys('test01@mail.ru')
# email_value = email.get_attribute('value')
# assert 'test01@mail.ru'in email_value
#
# address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
# address.clear()
# address.send_keys('test01_address')
# address_value = address.get_attribute('value')
# assert 'test01_address'in address_value

# driver.get('http://the-internet.herokuapp.com/status_codes')
# links_st = driver.find_elements(By.XPATH, '//li/a')
# for link in links_st:
#     link.click()
#     time.sleep(3)
#     driver.back()

driver.get('http://the-internet.herokuapp.com/status_codes')
for item in [200, 301, 404, 500]:
    driver.find_element(By.XPATH, f'//li/a [contains(text(), "{item}")]').click()
    driver.back()
