import math
from selenium import  webdriver

link="http://suninjuly.github.io/math.html"

browser=webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x=browser.find_element_by_id("input_value")
x=x.text
y=calc(x)

input_x=browser.find_element_by_id("answer")
input_x.send_keys(y)

robot_label=browser.find_element_by_css_selector("[for='robotCheckbox']")
robot_label.click()

check_box=browser.find_element_by_css_selector("[for='robotsRule']")
check_box.click()

button=browser.find_element_by_class_name("btn-default")
button.click()



