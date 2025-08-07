from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:

    link_browser = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    people_radio = browser.find_element(By.ID ,"peopleRule")
    people_checked = people_radio.get_attribute("checked") # возрощает значение атребута по умолчанию
    print("значени атребута 'people_radio' = ", people_checked)

    robot_radio = browser.find_element(By.ID ,"robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("значени атребута 'robot_checked' = ", robot_checked)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_checked = button.get_attribute("disabled")
    print("значение атребута Button = ",  button_checked )

    #assert people_checked is not None, "Если атребут Радиобаттон 'People rule' не == 'None' то Радиобаттон 'People rule'   выбрано не по умалчанию"
    assert people_checked == "true", "EEли приходит ошибка: 'rpeople_checked  == true' то атребут радиобаттон 'Peopl rule' не равен 'true' и радиобаттон 'Peopl rule' стоит НЕ ПО УМОЛЧАНИЮ!!!"

    #assert  robot_checked is not None, "Если атребут Радиобаттон 'Robot rule' не == 'None' то Радиобаттон 'Robot rule'   выбрано не  по умалчанию"
    assert  robot_checked == "true", "Eли приходит ошибка: 'robot_checked  == true' то атребут радиобаттон 'Robot rule' не равен 'true' и радиобаттон 'Robot rule' стоит НЕ ПО УМОЛЧАНИЮ!!!"

    
    
    # button_click = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    # button_click.click()

    
finally:

    time.sleep(60)
    browser.quit()    