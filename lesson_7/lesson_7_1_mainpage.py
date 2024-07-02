from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():

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

      
    def fill_field(self, FieldName, FieldValue):
        Fname = self.driver.find_element(By.NAME, FieldName) 
        Fname.send_keys(FieldValue)

    def press_button(self, selector):
        submit = self.driver.find_element(By.XPATH, selector)
        submit.click()
    
    def open_url(self, url):
        self.driver.get(url)
    
    def close_driver(self):
        self.driver.quit()

    def zipcode_color(self):
        zip = self.driver.find_element(By.ID, 'zip-code')
        zip_color =  zip.value_of_css_property("color")
        return zip_color

    # Ищем все элемены по css
    def find_elements(self, css_selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        return elements