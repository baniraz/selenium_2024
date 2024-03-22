from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://hyperskill.org/tracks')

driver.find_element(By.XPATH, "//div//a/ya-tr-span[@data-value=' Python ']")
driver.find_element(By.XPATH, "//div//*[@data-value=' Python ']")
driver.find_element(By.XPATH, '//div//a[@aria-label="Python Core"]//div[@class="card-badges"]')
