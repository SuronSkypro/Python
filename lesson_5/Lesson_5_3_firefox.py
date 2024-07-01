from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Firefox()
browser.get("http://uitestingplayground.com/classattr")

button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()


browser.quit()
