from selenium import webdriver
from typing import List
from selenium.webdriver.remote.webelement import WebElement  # Добавлено
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    """
        Класс для работы с web страницей 
    """

    def __init__(self, browser='chrome', *args, **kwargs):
        self.driver = self._init_driver(browser, *args, **kwargs)

    def _init_driver(self, browser: str, *args, **kwargs):
        """
            запускает Web браузер указаный в browser
        """
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

      
    def fill_field(self, FieldName: str , FieldValue: str):
        """
            Заполнение поля [FieldName] значением [FieldValue] на web странице
        """

        Fname = self.driver.find_element(By.NAME, FieldName) 
        Fname.send_keys(FieldValue)

    def press_button(self, selector: str ):
        """
            Нажатие кнопки на странице по сеелектору XPATH
        """

        submit = self.driver.find_element(By.XPATH, selector)
        submit.click()  
    
    def open_url(self, url:str):
        """
            Открывает страницу по адресу [url]
        """
        self.driver.get(url)
    
    def close_driver(self):
        """
            Закрывает браузер
        """
        self.driver.quit()

    def zipcode_color(self) -> str:
        """
            Возврашает цвет web элемента zip-code
        """
        zip = self.driver.find_element(By.ID, 'zip-code')
        zip_color =  zip.value_of_css_property("color")
        return zip_color

    # Ищем все элемены по css
    def find_elements(self, css_selector:str) -> List[WebElement]:
        """
            Возврашает web элемент  по сеелектору css_selector
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        return elements