from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element_by_css_selector('button').click()
alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_id('input_value').text
res = calc(x)

input = browser.find_element_by_id('answer')
input.send_keys(res)

button = browser.find_element_by_css_selector('button')
button.click()
