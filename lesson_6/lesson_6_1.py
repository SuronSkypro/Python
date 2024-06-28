from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


browser = webdriver.Firefox()

browser.get('http://uitestingplayground.com/ajax')


button = browser.find_element(By.ID, 'ajaxButton') 
button.click()

waiter = WebDriverWait(browser, 30)

label = waiter.until(
    EC.presence_of_element_located((By.ID, 'content')) 
)  

waiter.until(lambda driver: label.text != '')

print("текст плашки - ", label.text)




browser.quit()

