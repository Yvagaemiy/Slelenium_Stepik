#Открыть страницу https://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:

    link_browser = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    x = browser.find_element(By.ID, "input_value")
    x_num=x.text
    print("x = ",x_num)

    def calc(x_num):
        return str(math.log(abs(12*math.sin(int(x_num)))))
    print("решение по формуле = ", calc(x_num))

    answer_fild=browser.find_element(By.ID, "answer")
    answer_fild.send_keys(calc(x_num))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)#заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым
    checkbox.click()

    robotsrule = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsrule)#заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым
    robotsrule.click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)#заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым
    #  browser.execute_script("window.scrollBy(0, 100);") # Эта команда проскроллит страницу на 100 пикселей вниз
    button.click()

finally:

    time.sleep(10)
    browser.quit()   