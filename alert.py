from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    x = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(x)

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(6)
    browser.quit()

