import platform
import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

driver.get('https://the-internet.herokuapp.com/key_presses')

KEYBOARD_INPUT = (By.XPATH, '//input[@id="target"]')


driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(*KEYBOARD_INPUT).send_keys('FGFGHFGHFGFJFGHF')
driver.find_element(*KEYBOARD_INPUT).send_keys(CMD_CTRL + 'A')
time.sleep(2)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(2)


SELECT_LOCATOR = (By.XPATH, '//input[@id="react-select-3-input"]')
driver.get('https://demoqa.com/select-menu')
time.sleep(2)
driver.find_element(*SELECT_LOCATOR).send_keys('Ms.')
time.sleep(2)
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)

SELECT_ONE = (By.XPATH, '//div[@id="selectOne"]')
PROF_OPTION = (By.XPATH, '//div[text()="Prof."]')
driver.get('https://demoqa.com/select-menu')
time.sleep(2)
driver.find_element(*SELECT_ONE).click()
time.sleep(2)
driver.find_element(*PROF_OPTION).click()
time.sleep(2)


MULTISELECT_LOCATOR = (By.XPATH, '//input[@id="react-select-4-input"]')
driver.get('https://demoqa.com/select-menu')
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Green')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Bla')
assert driver.find_element(*MULTISELECT_LOCATOR).get_attribute("value") == "Bla", "Текст не введен"
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)

MULTISELECT_LOCATOR = (By.XPATH, '//input[@id="react-select-4-input"]')
driver.get('https://demoqa.com/select-menu')
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Gre')
time.sleep(2)
assert driver.find_element(*MULTISELECT_LOCATOR).get_attribute("value") == "Gre", "Текст не введен"
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)


driver.get("https://clipboardjs.com/")
COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")
COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)

PASTE.send_keys(CMD_CTRL + "A") # Выделим все внутри поля
time.sleep(2)
PASTE.send_keys(CMD_CTRL + "X") # Вырежем весь текст
time.sleep(2)
PASTE.send_keys(CMD_CTRL + "V") # Вставим весь текст

# setTimeout(function() { debugger; }, 5000); - включит отложенный старт дебаг-режима в devtools.


driver.get("https://demoqa.com/select-menu")
driver.find_element("xpath", "//div[@id='withOptGroup']").click() # Открываем dropdown
def choose_dropwdown_element_by_text(text): # Будем искать элемент внутри dropdown по тексту
    elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
    for element in elements:
        if text in element.text:
            return element # Возвращаем нужный элемент из dropdown по тексту

choose_dropwdown_element_by_text("Another root option").click() # Кликаем на выбранный элемент

