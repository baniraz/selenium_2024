from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Если не работает код выше
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
# driver.get('http://google.com/')

