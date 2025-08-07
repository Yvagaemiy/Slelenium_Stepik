from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:

    link_browser = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    num_1 = browser.find_element(By.ID, "num1")
    a_num_1=num_1.text
    print("num1 = ",a_num_1)

    num_2 = browser.find_element(By.ID, "num2")
    b_num_2=num_2.text
    print("num2 = ",b_num_2)
    
    c = int(a_num_1) + int(b_num_2)
    print("сумма чисел (num1 + num2) = ",c)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))
    
    button= browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
finally:

    time.sleep(10)
    browser.quit()    