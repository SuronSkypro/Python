from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


browser= webdriver.Chrome()
browser.get('http://uitestingplayground.com/dynamicid')

time.sleep(2)
i=1

while i < 4:
    browser.refresh()
    button = browser.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]')
    button.click()
    print("ID кнопки : ",str(button.get_attribute('id')))
    time.sleep(1)
    i=i+1


time.sleep(2)
browser.quit()




