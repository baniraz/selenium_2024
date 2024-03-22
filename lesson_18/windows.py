import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

BUSINESS_BTN_LOCATOR = (By.XPATH, '(//a[text()="For Business"][1])')
START_FREE_BTN_LOCATOR = (By.XPATH, '(//a[text()="Start for Free"])')

driver.get('https://hyperskill.org/tracks')
time.sleep(3)

driver.find_element(*BUSINESS_BTN_LOCATOR).click()
time.sleep(3)

tab = driver.window_handles # Записываем список открытых окон в переменную
driver.switch_to.window(tab[1])
time.sleep(3)

driver.find_element(*START_FREE_BTN_LOCATOR).click()
time.sleep(3)

driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
time.sleep(3)

driver.get('https://ya.ru')

# Дескриптор
current_tab = driver.current_window_handle
print(current_tab)

driver.get("https://hyperskill.org/login")
main_tab = driver.current_window_handle
START_FOR_FREE_BUTTON = ("xpath", "(//a[text()='Start for Free'])[1]")
driver.find_element(*START_FOR_FREE_BUTTON).click()
list_of_tabs = driver.window_handles # Пример списка ['CDwindow-0DE2EBAE188B1D6CDFAD2DEFF8A1E552', 'CDwindow-A0009183FCA5A328C2DBF38E3E812231']
driver.switch_to.window(list_of_tabs[1]) # Подставит дескриптор по индексу 1, т.е второй элемент списка
second_tab = driver.current_window_handle # Запишем дескриптор вкладки, на которую переключились выше
assert second_tab != main_tab, "Ошибка переключения между вкладками"

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows)) # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()


driver.quit() # Закрытие сессии, т.е всего браузера
driver.close() # Закрытие активного окна / вкладки
