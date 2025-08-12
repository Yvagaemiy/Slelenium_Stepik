#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
#Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #as EC
from selenium import webdriver
import math
import time

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    #ждем когдп прайс станет 100 долларов
    #WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "<От кого ждем>"), "<Что ждем>"))
    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"),"$100"))

    #ищем кнопку и жмем ее
    button = browser.find_element(By.ID, "book")
    button.click()

    #поиск не известного
    x_num = browser.find_element(By.ID, "input_value")
    x = x_num.text
    print("не известное число",x)
    #решаем функцию
    def calck(x):
        return str(abs(math.log(12 * math.sin(int(x)))))
    print("решение функции = ",calck(x))

    #поиск поля для ответа
    answe_serch = browser.find_element(By.ID,"answer")
    ride_answe= answe_serch.send_keys(calck(x))
    print(ride_answe)


    #жмем на кнопку
    submit_btn = browser.find_element(By.ID,"solve")
    submit_btn.click()
finally:

    time.sleep(15)
    browser.quit

