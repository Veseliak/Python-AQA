from  selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

try:
    link="http://suninjuly.github.io/selects2.html"

    driver = webdriver.Chrome()
    driver.get(link)

    a = int(driver.find_element_by_id("num1").text)
    b = int(driver.find_element_by_id("num2").text)
    c = str(a + b)

    select=Select(driver.find_element_by_id("dropdown"))
    select.select_by_value(c)

    driver.find_element_by_class_name("btn-default").click()

finally:
    time.sleep(5)
    driver.quit()