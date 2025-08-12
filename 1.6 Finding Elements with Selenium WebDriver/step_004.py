#Задание: поиск элементов с помощью Selenium
#Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.
#!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.
#!Кроме того, ограничено время на ввод ответа. Постарайтесь вводить ответ сразу.
#Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения для поиска вместо слов value1, value2 и т.д. Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(10)
    
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
    input3.send_keys("Smolensk@Russia.ru")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#NoSuchElementException