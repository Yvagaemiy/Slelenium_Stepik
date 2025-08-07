#Открыть страницу https://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:

    link_browser = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print("X = ",x)

    def calc(x):
        return str(math.log(abs(12 *math.sin(int(x)))))
    print("число = ",calc(x))
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(calc(x))

    checkbox_find = browser.find_element(By.ID,"robotCheckbox")
    checkbox_find.click()

    radiobutton_find = browser.find_element(By.ID ,"robotsRule")
    radiobutton_find.click()

    button_click = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_click.click()

    
finally:

    time.sleep(60)
    browser.quit()    