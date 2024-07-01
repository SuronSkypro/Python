from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/inputs")


input = browser.find_element(By.TAG_NAME, "input")

input.send_keys("1000")


input.clear()


input.send_keys("999")


browser.quit()
