from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/entry_ad")


button = browser.find_element(
    By.XPATH, '//div[@class="modal-footer"]/p[text()="Close"]'
)

button.click()


browser.quit()
