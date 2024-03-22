import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')

url = driver.current_url
print('URL страницы: ', url)
assert url == 'https://www.wikipedia.org/', 'Ошибка в URL'

current_title = driver.title
print('Текущий заголовок:', current_title)
assert current_title == 'Wikipedia', 'Некорректный заголовок'
# print(driver.page_source)

time.sleep(3)

driver.get('https://vk.com')
current_title = driver.title
print('Текущий заголовок:', current_title)
driver.get('https://ya.ru')
current_title_2 = driver.title
print('Текущий заголовок_2:', current_title_2)
time.sleep(3)
driver.back()
assert current_title == 'ВКонтакте | Добро пожаловать'
driver.refresh()
url = driver.current_url
driver.forward()
url_2 = driver.current_url
assert url != url_2
