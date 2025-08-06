#Задание
#На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

#Добавьте в самый верх своего кода import math
#Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
#Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
#str(math.ceil(math.pow(math.pi, math.e)*10000))
#(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) 
#Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link_element = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_element .click()
    #link_click = link_element.text
    #print("Содержимое: ", link_click )
    input1 = browser.find_element(By.TAG_NAME, "input") # по первому совпадению тега
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city") #в классе между словами обязательно поставить точкцу
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(2)
    browser.quit()
