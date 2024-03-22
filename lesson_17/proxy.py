import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY_SEERVER = 'username:password@37.19.220.129:8443' # Указываем адрес прокси-сервера
options = Options()
options.add_argument(f'--proxy-server={PROXY_SEERVER}') # Добавляем прокси через опции
driver = webdriver.Chrome(options=options)

driver.get('https://2ip.ru') # Проверяем IP-адрес

time.sleep(5)

# бесплатные прокси: http://free-proxy.cz/ru/