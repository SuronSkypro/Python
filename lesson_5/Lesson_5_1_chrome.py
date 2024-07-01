from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/add_remove_elements/")


temp__ = "button[onclick*='addElement']"
button = browser.find_element(By.CSS_SELECTOR, temp__)
button.click()
button.click()
button.click()
button.click()
button.click()
button.click()


buttons = browser.find_elements(By.CLASS_NAME, "added-manually")

# Подсчитываем количество найденных кнопок
count = len(buttons)
print("Количество кнопок с классом 'added-manually':", count)

print(str(len))


time.sleep(10)
browser.quit()
