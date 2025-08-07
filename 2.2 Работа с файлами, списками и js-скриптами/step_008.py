#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
#import math

try:
    link_browser = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    serch_firstname=browser.find_element(By.NAME,"firstname")
    serch_firstname.send_keys("Ivan")

    serch_lastname=browser.find_element(By.NAME,"lastname")
    serch_lastname.send_keys("Ivanov")
    
    serch_email=browser.find_element(By.NAME,"email")
    serch_email.send_keys("ivanov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'my_file.txt')           # добавляем к этому пути имя файла 
    serch_file = browser.find_element(By.ID,"file")
    serch_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

finally:

    time.sleep(10)
    browser.quit