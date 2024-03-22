import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://the-internet.herokuapp.com/drag_and_drop')

COLLUMN_A = (By.XPATH, '//div[@id="column-a"]')
COLLUMN_B = (By.XPATH, '//div[@id="column-b"]')

A = driver.find_element(*COLLUMN_A)
B = driver.find_element(*COLLUMN_B)
time.sleep(3)
action.drag_and_drop(A, B).perform()
time.sleep(3)


driver.get('https://tympanus.net/Development/DragDropInteractions/sidebar.html')

GRID = (By.XPATH, '(//div[@class="grid__item"])[3]')
SIDEBAR = (By.XPATH, '(//div[@class="drop-area__item"])[3]')

action.click_and_hold(driver.find_element(*GRID)) \
    .pause(2) \
    .move_to_element(driver.find_element(*SIDEBAR)) \
    .release().perform()
time.sleep(3)



driver.get("https://demoqa.com/sortable")
SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source) # Находим source-элемент
    TARGET = driver.find_element(*target) # Находим target-элемент
    wait.until(EC.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем

drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR) # Использование функции
