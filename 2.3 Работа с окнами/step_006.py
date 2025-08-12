#Задание: переход на новую вкладку

#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import math

try:
    link_browser = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()
    print("browser.window_handles сколько страниц в списке",browser.window_handles) # узнаем список страниц сайта
    second_window = browser.window_handles[1]
    print("new_window страница 1 = ",second_window)

    browser.switch_to.window(second_window) #Для переключения на новую вкладку

    scerh_x = browser.find_element(By.ID,"input_value")
    x = scerh_x.text
    print('не известная х = ',x)

    def calc(x):
        return str(math.log(12*math.sin(int(x))))
    print('расчет функции от х = ',x)

    serch_answer = browser.find_element(By.ID,"answer")
    serch_answer.send_keys(calc(x))

    button_2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button_2.click()

    #alert= browser.switch_to.alert
    #alert.accept()

    
    
finally:

    time.sleep(10)
    browser.quit