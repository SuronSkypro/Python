from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


browser = webdriver.Firefox()

browser.get('http://uitestingplayground.com/textinput')


temptxt = browser.find_element(By.ID, 'newButtonName') 
temptxt.send_keys("Skypro")

button = browser.find_element(By.ID, 'updatingButton') 
button.click()

print("текст кнопки - ", button.text)


browser.quit()

