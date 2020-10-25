from selenium import webdriver
import time
import math

LINK="http://suninjuly.github.io/get_attribute.html"

driver=webdriver.Chrome()
driver.get(LINK)

try:
    def func(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = driver.find_element_by_id("treasure")
    x = x.get_attribute("valuex")

    y = func(x)

    line = driver.find_element_by_id("answer")
    line.send_keys(y)

    check = driver.find_element_by_id("robotCheckbox")
    check.click()

    radio = driver.find_element_by_id("robotsRule")
    radio.click()

    btn = driver.find_element_by_class_name("btn-default")
    btn.click()


finally:
    time.sleep(5)
    driver.quit()