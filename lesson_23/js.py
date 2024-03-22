import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from scrolls import Scrolls


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()
action = ActionChains(driver)
scroll = Scrolls(driver, action)

# driver.get('https://seiyria.com/bootstrap-slider/')
# driver.execute_script('alert("Hello")') # Вызов js-кода на странице
# time.sleep(3)

driver.get('https://seiyria.com/bootstrap-slider/')
EX2_LOC = ('xpath', '//h3[text()="Example 2: "]')
EX2 = driver.find_element(*EX2_LOC)
scroll.scroll_to_element(EX2)

time.sleep(3)

