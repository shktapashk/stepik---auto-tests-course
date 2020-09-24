from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Код, который определяет, когда цена уменьшится до 100$
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book").click()
    
    #Код, который скроллит до следующего поля
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #Код, который получает значение x
    xvalue = browser.find_element_by_id("input_value")
    x = xvalue.text

    #Код, который считает формулу
    y = calc(x)

    #Код, которые находит форму в которую нужно ввести ответ и вводит его
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
         
    # Отправляем заполненную форму
    button1 = browser.find_element_by_id("solve").click()
   
             
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
