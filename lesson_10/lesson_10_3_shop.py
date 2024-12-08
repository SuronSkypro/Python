from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ShopPage():

    def __init__(self, browser='chrome', *args, **kwargs):
        self.driver = self._init_driver(browser, *args, **kwargs)

    def _init_driver(self, browser, *args, **kwargs):
        if browser.lower() == 'chrome':
            return webdriver.Chrome(*args, **kwargs)
        elif browser.lower() == 'firefox':
            return webdriver.Firefox(*args, **kwargs)
        elif browser.lower() == 'safari':
            return webdriver.Safari(*args, **kwargs)
        elif browser.lower() == 'edge':
            return webdriver.Edge(*args, **kwargs)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)
    
    def close_driver(self):
        self.driver.quit()


    def autorize(self, username, password):
           
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_item_to_cart_BY_ID(self, id):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id))).click()

    def click_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def click_button_BY_ID(self, id):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id))).click()
    
    def fill_field_BY_ID(self, id, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id))).send_keys(text)
                                                                                                    
    def return_text_BY_CLASS_NAME(self, class_name):
        return WebDriverWait(self.driveer, 10).until(EC.presence_of_element_located((By.CLASS_NAME,class_name ))).text
        













   

    def press_button_BY_XPATH(self, selector):
        submit = self.driver.find_element(By.XPATH, selector)
        submit.click()
    
   

    def return_text_BY_CLASS_NAME(self, field):
        return self.driver.find_element(By.CLASS_NAME, field).text
    
    def wait_present_element_BY_CLASS_NAME(self, field):
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, field), "15"))

    def fill_element_BY_ID(self,id,str):
        delay = self.driver.find_element(By.ID,id)
        delay.clear()
        delay.send_keys(str)



    