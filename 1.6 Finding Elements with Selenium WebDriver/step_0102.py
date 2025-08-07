
#Открыть страницу http://suninjuly.github.io/get_attribute.html.
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#Посчитать математическую функцию от x (сама функция остаётся неизменной).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку "Submit".


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:

    link_browser = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    img_find = browser.find_element(By.ID,"treasure")
    sekret_img_find = img_find.get_attribute("valuex")
    print("Код из сундука = ",sekret_img_find)

    def calc(sekret_img_find):
       return str(math.log(abs(12 *math.sin(int(sekret_img_find)))))
    print("число = ",calc(sekret_img_find))
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(calc(sekret_img_find))

    checkbox_find = browser.find_element(By.ID,"robotCheckbox")
    checkbox_find.click()

    radiobutton_find = browser.find_element(By.ID ,"robotsRule")
    radiobutton_find.click()

    button_click = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_click.click()

    
finally:

    time.sleep(60)
    browser.quit()    