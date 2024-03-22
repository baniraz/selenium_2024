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

FORM_NAME_LOC = (By.XPATH, '//input[@id="RESULT_TextFIELD-0"]')
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.switch_to.frame('frame-one796456169')
# time.sleep(3)
# driver.find_element(*FORM_NAME_LOC).send_keys('Test1')
# time.sleep(3)

# iframe_volunteer = driver.find_element(By.XPATH, "//iframe")
# driver.switch_to.frame(iframe_volunteer)
# first_name_field = driver.find_element(By.XPATH, "//input[@name='RESULT_TextField-1']")
# first_name_field.send_keys("Test1")
#
# driver.switch_to.default_content() # Переключение с iframe обратно на страницу

# COPY_TEXT = (By.XPATH, '//button[@ondblclick="myFunction1()"]')
# driver.find_element(*COPY_TEXT).click()


driver.get('https://demoqa.com/nestedframes')
driver.switch_to.frame('frame1')
print(driver.find_element(By.XPATH, '//body').text)

driver.switch_to.frame(0)
print(driver.find_element(By.XPATH, '//body').text)

driver.switch_to.parent_frame()
print(driver.find_element(By.XPATH, '//body').text)

driver.switch_to.default_content()