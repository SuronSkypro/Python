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

#time.sleep(10)

submit = browser.find_element(By.CLASS_NAME, "btn btn-outline-primary mt-3")
submit.click()


time.sleep(55)

browser.quit()

