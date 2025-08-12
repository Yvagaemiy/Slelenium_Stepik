#Есть способы получше: Selenium Waits (Implicit Waits)

from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(5) #позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:

    browser.quit