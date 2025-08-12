#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#Принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import math

try:
    link_browser = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept() #согласие
    #confirm.dismiss() # отказ

    serhc_x = browser.find_element(By.ID, "input_value")
    teke_x = serhc_x.text
    print("ускомое число = ",teke_x)

    def colum(teke_x):
        return str(math.log((abs(12*math.sin(int(teke_x ))))))
    print("ответ по формуле",colum(teke_x))

    serhc_field = browser.find_element(By.ID,"answer")
    serhc_field.send_keys(colum(teke_x))

    button = browser.find_element(By.CSS_SELECTOR,"button.btn.btn-primary")
    button.click()

    #alert= browser.switch_to.alert
    #alert.accept()
finally:

    time.sleep(10)
    browser.quit