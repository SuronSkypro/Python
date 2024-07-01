from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/login")


input = browser.find_element(By.ID, "username")
input.send_keys("tomsmith")


input = browser.find_element(By.ID, "password")
input.send_keys("SuperSecretPassword!")


but = browser.find_element(By.CSS_SELECTOR, "button.radius")
but.click()


browser.quit()
