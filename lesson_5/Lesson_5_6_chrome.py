from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


browser= webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')


input = browser.find_element(By.ID, 'username')
input.send_keys("tomsmith")
time.sleep(5)

input = browser.find_element(By.ID, 'password')
input.send_keys("SuperSecretPassword!")

time.sleep(2)

but= browser.find_element(By.CSS_SELECTOR, 'button.radius')
but.click()


time.sleep(2)
browser.quit()