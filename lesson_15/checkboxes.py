import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHECKBOX_1 = (By.XPATH, '(//input[@type="checkbox"])[1]')

driver.get('https://the-internet.herokuapp.com/checkboxes')
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).get_attribute('checked'))
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).get_attribute('checked'))
print(type(driver.find_element(*CHECKBOX_1).get_attribute('checked')))
assert driver.find_element(*CHECKBOX_1).get_attribute('checked') is not None
assert driver.find_element(*CHECKBOX_1).get_attribute('checked') == 'true'

print(driver.find_element(*CHECKBOX_1).is_selected())
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).is_selected())
assert driver.find_element(*CHECKBOX_1).get_attribute('checked') is True


CHECKBOX_HOME_STATUS = (By.XPATH, '//input[@id="tree-node-home"]')
CHECKBOX_HOME_ACTION = (By.XPATH, '//span[@class="rct-checkbox"]')
driver.get('https://demoqa.com/checkbox')
print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
driver.find_element(*CHECKBOX_HOME_ACTION).click()
print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
assert driver.find_element(*CHECKBOX_HOME_STATUS).is_selected() is True

ELEMENT_ONE = (By.XPATH, '//li[text()="Cras justo odio"]')
driver.get('https://demoqa.com/selectable')
before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
print(before)
driver.find_element(*ELEMENT_ONE).click()
after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
assert 'active' in after

if 'active' in after:
    print("VSE OK")



driver.get('https://demoqa.com/radio-button')
YES_RADIO_STATUS = (By.XPATH, '//input[@id="yesRadio"]')
NO_RADIO_STATUS = (By.XPATH, '//input[@id="noRadio"]')
YES_RADIO_ACTION = (By.XPATH, '//label[@for="yesRadio"]')
NO_RADIO_ACTION = (By.XPATH, '//input[@id="noRadio"]')
driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_ACTION).is_selected())
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
print(driver.find_element(*YES_RADIO_STATUS).is_enabled())
assert driver.find_element(*YES_RADIO_STATUS).is_enabled() is True


driver.get('https://demoqa.com/selectable')
driver.find_element(By.XPATH, '//a[@data-rb-event-key="grid"]').click()
One = (By.XPATH, '//div[@id="row1"]//li[text()="One"]')
driver.find_element(*One).click()
Four = (By.XPATH, '//li[contains(text(), "Four")]')
driver.find_element(*Four).click()
assert "active" in driver.find_element(*One).get_attribute("class")
assert "active" in driver.find_element(*Four).get_attribute("class")
driver.find_element(*One).click()
driver.find_element(*Four).click()
assert "active" not in driver.find_element(*One).get_attribute("class")
assert "active" not in driver.find_element(*Four).get_attribute("class")