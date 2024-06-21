from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


browser= webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/inputs')

time.sleep(2)
input= browser.find_element(By.TAG_NAME, 'input')

input.send_keys("1000")
time.sleep(2)

input.clear()

time.sleep(2)

input.send_keys("999")

time.sleep(2)
browser.quit()

