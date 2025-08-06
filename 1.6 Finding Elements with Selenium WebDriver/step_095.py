from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")
time.sleep(30)
input1 = browser.find_element(By.CSS_SELECTOR, value = 'input+[placeholder="Input your first name"]')
input1.send_keys("Alex")
time.sleep(10)
input2 = browser.find_element(by = "css selector", value = 'input+[placeholder="Input your last name"]')
input2.send_keys("Karasev")
time.sleep(10)
input3 = browser.find_element(by = "css selector", value = 'input+[placeholder="Input your email"]')
input3.send_keys("alexx333karasev@yandex.ru")
time.sleep(10)
button = browser.find_element(by = "tag name", value = "button")
button.click()
time.sleep(10)

massage = browser.find_element(by = "tag name", value = "h1")
true_massage = massage.text

assert "Congratulations! You have successfully registered!" == true_massage
