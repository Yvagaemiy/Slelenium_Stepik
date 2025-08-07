from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
browser = webdriver.Chrome()

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'my_file.txt')           # добавляем к этому пути имя файла 
serch_file = browser.find_element(By.ID,"file")
serch_file.send_keys(file_path)