from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# User credentials and form data
username = "standard_user"
password = "secret_sauce"
first_name = "Александр"
last_name = "Недоростков"
postal_code = "440028"

browser = webdriver.Chrome()

try:
    browser.get("https://www.saucedemo.com/")

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Александр")
    browser.find_element(By.ID, "last-name").send_keys("Недоростков")
    browser.find_element(By.ID, "postal-code").send_keys("440028")
    browser.find_element(By.ID, "continue").click()

       
    total_amount = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    
    assert total_amount == "Total: $58.29"
    print("Общая сумма верная:", total_amount)


finally:
    
    browser.quit()