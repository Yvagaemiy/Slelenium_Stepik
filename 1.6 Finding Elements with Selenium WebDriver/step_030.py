#  browser.close() закрывает текущее окно браузера. 
#browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()