import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)


driver.get('https://hyperskill.org/login')
driver.switch_to.new_window('tab')
driver.get('https://www.avito.ru/')
driver.switch_to.new_window('tab')
driver.get('https://the-internet.herokuapp.com/dropdown')

windows = driver.window_handles
print(len(windows))

current_tab_2 = driver.current_window_handle
print("Индекс: ", windows.index(current_tab_2))

driver.switch_to.window(windows[0])
current_tab_0 = driver.current_window_handle
assert current_tab_2 != current_tab_0
PAGE_TITLE_1 = driver.title
print("Title страницы_1: ", PAGE_TITLE_1)

driver.switch_to.window(windows[1])
current_tab_1 = driver.current_window_handle
assert current_tab_0 != current_tab_1
PAGE_TITLE_2 = driver.title
print("Title страницы_2: ", PAGE_TITLE_2)

driver.switch_to.window(windows[2])
assert current_tab_1 != driver.current_window_handle
PAGE_TITLE_3 = driver.title
print("Title страницы_3: ", PAGE_TITLE_3)

driver.switch_to.window(windows[0])
assert current_tab_2 != driver.current_window_handle
time.sleep(5)
driver.find_element(By.XPATH, '//button[@data-cy="submitButton"]').click()
time.sleep(5)

driver.switch_to.window(windows[1])
time.sleep(5)
assert current_tab_0 != driver.current_window_handle
driver.find_element(By.XPATH, '//button[@data-marker="top-rubricator/all-categories"]').click()
time.sleep(5)

driver.switch_to.window(windows[2])
assert current_tab_1 != driver.current_window_handle
SELECT_LOCATOR = (By.XPATH, '//select[@id="dropdown"]')
driver.find_element(*SELECT_LOCATOR).send_keys('Option 1')
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(5)