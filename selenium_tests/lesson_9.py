from selenium import webdriver
import time
import math

try:
    link="http://suninjuly.github.io/alert_accept.html"

    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element_by_css_selector("[type='submit']").click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    x = driver.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()