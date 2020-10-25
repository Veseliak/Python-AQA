import os


a=os.path.abspath(os.path.dirname(__file__))
b=os.path.join(a, 'file.txt')
print(a +"\n"+ b)

# close allert
alert = browser.switch_to.alert
alert.accept()
#get allert text
alert = browser.switch_to.alert
alert_text = alert.text

#close confirm
confirm = browser.switch_to.alert
confirm.accept()
#confirm cencelation
confirm.dismiss()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

#prompt
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()


#switch to other window in browser
browser.switch_to.window(window_name)

#other window name
new_window = browser.window_handles[1]

#current window name
first_window = browser.window_handles[0]
