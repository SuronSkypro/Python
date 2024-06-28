from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Set up the driver (make sure the appropriate driver is installed and in your PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Locate the submit button by CSS Selector


submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")

# Optionally click the submit button
submit_button.click()

# Close the driver
driver.quit()