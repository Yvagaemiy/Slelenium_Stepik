from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.TAG_NAME, "input")
    input_first_name.send_keys("Ivan")
    input_emai = browser.find_element(By.CLASS_NAME, "form-control.third")
    input_emai.send_keys("ivan@mail.ru")

    labels_phon = browser.find_elements(By.TAG_NAME,'label') # Список лэйблов над текстовыми полями
    inputs_phon = browser.find_elements(By.TAG_NAME,'input') # Список текстовых полей

    for i, label in enumerate(labels_phon): 
        print("i(index) =",i)         
        if label.text in "Phone:":
            print("label.text(совподение!) =",label.text)               
            inputs_phon[i].send_keys("898678567456") 

    input_address = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
    input_address.send_keys("Уточкина, дом 2, кв 3")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print("Ответ при регестрации: ",welcome_text)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #Метод time.sleep(1) говорит Python подождать 1 секунду, прежде чем выполнять следующую строчку кода. Если вы всё равно видите эту ошибку, просто увеличьте количество секунд ожидания.
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()