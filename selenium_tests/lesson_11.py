from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import math

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

try:
    WebDriverWait(driver, 20).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    driver.find_element_by_id("book").click()
    x=driver.find_element_by_id("input_value").text
    driver.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    button = driver.find_element_by_id("solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    driver.quit()