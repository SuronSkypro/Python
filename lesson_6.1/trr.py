from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the target page
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types-submitted.html?first-name=%D0%B5%D0%BD%D0%BE&last-name=%D0%BE%D0%BF%D0%B0%D0%B2%D0%BF%D1%80&address=%D0%BF%D0%B0%D0%BE%D0%BF%D0%B0&zip-code=&city=%D0%B0%D0%BF%D0%B2%D0%BE&country=%D0%B0%D0%BF%D0%BE&e-mail=frg%40rr.com&phone=%D0%B0%D0%BF%D0%BE%D0%B2&job-position=%D0%BE%D0%B0%D0%B2%D0%BF&company=%D0%B0%D0%B2%D0%BF%D0%BE")

    # Locate the ZIP code field
    zip_code_field = driver.find_element(By.XPATH, "/class[textzip-code")  # Replace with the actual locator if different

    # Get the background color of the ZIP code field
    background_color = zip_code_field.value_of_css_property("background-color")

    # Print the background color value
    print("ZIP code field background color:", background_color)

    # Get the text color of the ZIP code field (if needed)
    text_color = zip_code_field.value_of_css_property("color")
   
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()