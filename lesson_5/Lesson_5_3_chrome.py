from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


browser= webdriver.Chrome()
browser.get('http://uitestingplayground.com/classattr')

time.sleep(2)
button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()


time.sleep(2)
browser.quit()

