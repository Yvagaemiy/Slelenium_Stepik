#Способ с функцией time.sleep()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(5)# кнопка появляется с задержкой, мы можем добавить паузу до начала поиска элемента
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:

    
    browser.quit