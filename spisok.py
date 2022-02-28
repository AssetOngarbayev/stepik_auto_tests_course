import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def sum(x, y):
    x = int(x)
    y = int(y)
    return str(x + y)
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    result = sum(a, b)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   
 
