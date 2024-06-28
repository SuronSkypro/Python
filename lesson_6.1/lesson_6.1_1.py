from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


browser = webdriver.Chrome()

browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


Fname = browser.find_element(By.NAME, 'first-name') 
Fname.send_keys("Иван")

Lname = browser.find_element(By.NAME, 'last-name') 
Lname.send_keys("Петров")

Address = browser.find_element(By.NAME, 'address') 
Address.send_keys("Ленина, 55-3")

Zip = browser.find_element(By.NAME, 'zip-code') 
Zip.send_keys("")

Email = browser.find_element(By.NAME, 'e-mail') 
Email.send_keys("test@skypro.com")

Phone = browser.find_element(By.NAME, 'phone') 
Phone.send_keys("+7985899998787")

City = browser.find_element(By.NAME, 'city') 
City.send_keys("Москва")

Country = browser.find_element(By.NAME, 'country') 
Country.send_keys("Россия")

Job = browser.find_element(By.NAME, 'job-position') 
Job.send_keys("QA")

Company = browser.find_element(By.NAME, 'company') 
Company.send_keys("SkyPro")

submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
submit.click()

# Проверка цветов

zip = browser.find_element(By.ID, 'zip-code')

text_color =  zip.value_of_css_property("color")
assert text_color == "rgba(132, 32, 41, 1)"
print("Цвет zip красный:", text_color)

alert_elements = browser.find_elements(By.CSS_SELECTOR, ".alert.py-2.alert-success")

for idx, element in enumerate(alert_elements):
    el_color = alert_elements[idx].value_of_css_property("color")
    assert el_color == "rgba(15, 81, 50, 1)"
    print ("Ok")



time.sleep(5)

browser.quit()

