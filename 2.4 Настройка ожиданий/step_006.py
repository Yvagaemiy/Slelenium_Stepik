from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/cats.html")
    browser.implicitly_wait(5) #позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам
    
    button = browser.find_element(By.ID, "button")
    button.click()
    #message = browser.find_element(By.ID, "button")

    #assert "StaleElementReferenceException" == True
    assert "NoSuchElementException" ,"нет такого вообще" 
    

finally:
    browser.quit
    

#except 'ElementNotVisibleException':
#    print("видишь элемент? И я не вижу, а он есть")

#except 'NoSuchElementException ':   
#    print("нет такого вообще")

#except 'MoveTargetOutOfBoundsException':
#   print("попытка взаимодействия с элементом, находящимся за пределами видимой области браузера")



