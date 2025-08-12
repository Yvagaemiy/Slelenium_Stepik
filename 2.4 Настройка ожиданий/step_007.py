#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(5)

#browser.get("http://suninjuly.github.io/wait2.html")

#button = browser.find_element(By.ID, "verify")
#button.click()
#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text

#no such element: Unable to locate element: {"method":"id","selector":"verify_message"}ищим эту ошибку


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.ID, "verify")))
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text