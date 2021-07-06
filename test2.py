from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

troll_btn = browser.find_element_by_class_name('trollface')
troll_btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id('input_value').text
res = calc(x)

input = browser.find_element_by_id('answer')
input.send_keys(res)

button = browser.find_element_by_css_selector('button')
button.click()