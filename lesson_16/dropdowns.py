import os
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = (By.XPATH, '//select[@id="dropdown"]')

driver.get('https://the-internet.herokuapp.com/dropdown')
DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(5)
# DROPDOWN.select_by_visible_text('Option 1')
# time.sleep(5)
#
# time.sleep(5)
# DROPDOWN.select_by_value('2')
# time.sleep(5)
#
# time.sleep(5)
# DROPDOWN.select_by_index('1')
# time.sleep(5)

all_options = DROPDOWN.options
print(all_options)

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_visible_text(option.text)

for option in all_options:
    time.sleep(2)
    if 'Option 2' in option.text:
        print('Opciya prisutstvuet')

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_index(all_options.index(option))

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_value(option.get_attribute('value'))


