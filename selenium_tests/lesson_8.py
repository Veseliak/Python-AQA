import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
driver.get(link)

try:
    driver.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("Name")
    driver.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("Last")
    driver.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("test@email.com")

    path=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(path, "debug.log")

    driver.find_element_by_id("file").send_keys(file_path)
    driver.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()

