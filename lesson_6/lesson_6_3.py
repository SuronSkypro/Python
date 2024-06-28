from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Firefox()

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


waiter = WebDriverWait(browser, 30)

images = waiter.until(EC.presence_of_element_located((By.ID, "landscape")))


print("Картинка появилась  ", images)
images = browser.find_element(By.ID, "award")
print("Атрибут - ", images.get_attribute("src"))


browser.quit()
