from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

def test_1():

        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5) #позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам

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
        print("Ответ при регестрации Тест№1 : ",welcome_text)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
        #assert "Congratulations! You have successfully registered!" == welcome_text, "Ok"
        assert "Congratulations! You have successfully registered!" == welcome_text, "test_1 Ок"

    # закрываем браузер после всех манипуляций
        browser.quit()

def test_2():

        link_2 = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link_2)
        browser.implicitly_wait(5) #позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам

    # Ваш код, который заполняет обязательные поля
        input_first_name_2 = browser.find_element(By.TAG_NAME, "input")
        input_first_name_2.send_keys("Ivan")
        input_emai_2 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input_emai_2.send_keys("ivan@mail.ru")

        labels_phon_2 = browser.find_elements(By.TAG_NAME,'label') # Список лэйблов над текстовыми полями
        inputs_phon_2 = browser.find_elements(By.TAG_NAME,'input') # Список текстовых полей

        for i, label in enumerate(labels_phon_2): 
            print("i(index) =",i)         
        if label.text in "Phone:":
            print("label.text(совподение!) =",label.text)               
            inputs_phon_2[i].send_keys("898678567456") 

        input_address = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
        input_address.send_keys("Уточкина, дом 2, кв 3")

    # Отправляем заполненную форму
        button_2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        button_2.click()
    
    # находим элемент, содержащий текст
        welcome_text_elt_2 = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_2 = welcome_text_elt_2.text
        print("Ответ при регестрации Тест№2 : ",welcome_text_2)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
        #assert "Congratulations! You have successfully registered!" == welcome_text_2, "Ok"
        assert  "Congratulations! You have successfully registered!" == welcome_text_2, "test_2 Ок"


    # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    pytest.main()