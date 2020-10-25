from selenium import webdriver
import math
import time


# driver.execute_script("document.title='Script executing'; alert('Robots at work');")
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# browser.execute_script("window.scrollBy(0, 100);") scroll by 100 pixels
link = "http://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)

try:


    def func(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = driver.find_element_by_id("input_value").text

    y = func(x)


    line = driver.find_element_by_id("answer")
    line.send_keys(y)

    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    check = driver.find_element_by_css_selector("[for='robotCheckbox']")
    check.click()

    radio = driver.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    btn = driver.find_element_by_class_name("btn-primary")
    btn.click()

finally:
    time.sleep(5)
    driver.quit()