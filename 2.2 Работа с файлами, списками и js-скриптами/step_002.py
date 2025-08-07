from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:

    link_browser = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link_browser)

    #a = browser.find_element(By.TAG_NAME, "select").click()
    #print("a=", a)
    #b = browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
    #print("b=", b)
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("73") # ищем элемент с текстом "Python"
    #browser.find_element(By.CSS_SELECTOR, "[value = '1']").click()
    
finally:

    time.sleep(1)
    browser.quit()    