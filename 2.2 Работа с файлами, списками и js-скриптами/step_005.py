from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)#заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым
    #  browser.execute_script("window.scrollBy(0, 100);") # Эта команда проскроллит страницу на 100 пикселей вниз
    button.click()

finally:
    
    time.sleep(10)
    browser.quit
