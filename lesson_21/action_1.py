import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_BTN_LOC = (By.XPATH, '//button[@id="leftClick"]')
DOUBLE_BTN_LOC = (By.XPATH, '//button[@id="leftClick"]')
RIGHT_BTN_LOC = (By.XPATH, '//button[@id="leftClick"]')
HOVER_BTN_LOC = (By.XPATH, '//button[@id="colorChangeOnHover"]')

driver.get('https://testkru.com/Elements/Buttons')
left_btn = driver.find_element(*LEFT_BTN_LOC)
double_btn = driver.find_element(*DOUBLE_BTN_LOC)
right_btn = driver.find_element(*RIGHT_BTN_LOC)
hover_btn = driver.find_element(*HOVER_BTN_LOC)


# time.sleep(3)
# action.click(left_btn).perform()
# action.click(double_btn).perform()
# action.click(right_btn).perform()
# time.sleep(3)
#
# time.sleep(3)
# action.click(left_btn).double_click(double_btn).context_click(right_btn).perform()
# time.sleep(3)

# time.sleep(3)
# action.click(left_btn).pause(2).double_click(double_btn).pause(2).context_click(right_btn).perform()
# time.sleep(3)

# action.move_to_element(hover_btn).perform()

driver.get('https://demoqa.com/menu')
MENU_2_LOC = (By.XPATH, '//ya-tr-span[@data-value="Main Item 2"]')
SUB_LOC = (By.XPATH, '//a[text()="SUB SUB LIST »"]')

menu_2 = driver.find_element(*MENU_2_LOC)
sub = driver.find_element(*SUB_LOC)

action.move_to_element(menu_2) \
    .pause(3).move_to_element(sub) \
    .perform()

time.sleep(3)


driver.get("https://clipboardjs.com/")
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
action.scroll_to_element(SOME_ELEMENT).perform() # Используем скролл до элемента