from selenium import webdriver
import math
import time

link="http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(link)

try:
    driver.find_element_by_css_selector('[type="submit"]').click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
