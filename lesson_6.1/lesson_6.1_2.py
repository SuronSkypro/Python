from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the web driver
browser = webdriver.Chrome()

try:
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Allow some time for the page to load
    time.sleep(2)

    delay = browser.find_element(By.ID,"delay")
    delay.clear()
    delay.send_keys("45")

    button_7 = browser.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_plus = browser.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = browser.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_equals = browser.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    WebDriverWait(browser, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    
    
    result = browser.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"
    print("Ok")
    
finally:
    
    browser.quit()