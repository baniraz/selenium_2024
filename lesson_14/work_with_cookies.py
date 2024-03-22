import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# driver.get('https://www.freeconferencecall.com/en/us/login')
# print(driver.get_cookies())
# driver.add_cookie({
#     'name': 'Example',
#     'value': 'Kukushka'
# })
# print(driver.get_cookie("Example"))
# driver.delete_cookie("Example")
# driver.add_cookie({
#     'name': 'Example',
#     'value': 'More'
# })
# print(driver.get_cookie("Example"))

# driver.get("https://www.freeconferencecall.com/en/us/login")
# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
# driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.find_element(*LOGIN_FIELD).send_keys("cestsecret@mail.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("test123")
# driver.find_element(*SUBMIT_BUTTON).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# driver.get("https://www.freeconferencecall.com/login")
# driver.delete_all_cookies()

# # Открываем страницу логина
# driver.get("https://www.freeconferencecall.com/profile")
#
# # Чистим все куки
# driver.delete_all_cookies()
#
# # Записываем куки из файла в переменную
# cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
#
# # Добавляем по одной куке из списка
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# # Делаем запрос на любую страницу залогиненного пользователя
# driver.get("https://www.freeconferencecall.com/profile")

#
# LOGIN_FIELD = ("xpath", "//input[@id='username']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//input[@name='login']")
# driver.get("https://rishon.store/my-account-2/")
# driver.find_element(*LOGIN_FIELD).send_keys("cestsecret@mail.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("bZ6&ot&W84*2")
# driver.find_element(*SUBMIT_BUTTON).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies1.pkl", "wb"))
# print(driver.get_cookies())
# driver.add_cookie({
#     'name': 'username',
#     'value': 'user123'
# })
# driver.refresh()
# print(driver.get_cookie("username"))
# name_cookie = driver.get_cookie("username")
# assert 'user123' == name_cookie['value']
# print(name_cookie['value'])
#
# LOGIN_FIELD = ("xpath", "//input[@id='username']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//input[@name='login']")
# driver.get("https://rishon.store/my-account-2/")
# driver.find_element(*LOGIN_FIELD).send_keys("cestsecret@mail.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("bZ6&ot&W84*2")
# driver.find_element(*SUBMIT_BUTTON).click()
# all_cookies = driver.get_cookies()
# print(all_cookies)
# for cookie in all_cookies:
#     print(cookie['name'])
# name_cookie = driver.get_cookie("pys_landing_page")
# print(name_cookie)
# driver.delete_cookie('pys_landing_page')
# driver.refresh()
# all_cookies = driver.get_cookies()
# print(all_cookies)
# for cookie in all_cookies:
#     assert name_cookie['name'] != cookie['name']


LOGIN_FIELD = ("xpath", "//input[@name='email']")
PASSWORD_FIELD = ("xpath", "//input[@name='password']")
SUBMIT_BUTTON = ("xpath", "//input[@name='login']")
driver.get("https://deliherb.ru/user/login")
driver.find_element(*LOGIN_FIELD).send_keys("cestsecret@mail.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("test123")
driver.find_element(*SUBMIT_BUTTON).click()
driver.find_element(By.XPATH, '//a[@title="Состояния здоровья"][@data-category="3"]').click()
driver.find_element(By.XPATH, '//a[@data-product="5231"]').click()
driver.find_element(By.XPATH, '//input[@class="button iherb l"]').click()
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies3.pkl", "wb"))
driver.delete_all_cookies()
driver.refresh()
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies3.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
