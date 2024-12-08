from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CalcPage():

    def __init__(self, browser='chrome', *args, **kwargs):
        self.driver = self._init_driver(browser, *args, **kwargs)

    def _init_driver(self, browser, *args, **kwargs):
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

    
   

    def press_button_BY_XPATH(self, selector: str):
        """
            Нажатие кнопки на странице по сеелектору XPATH
        """
        submit = self.driver.find_element(By.XPATH, selector)
        submit.click()
    
    def open_url(self, url: str):
        """
            Открывает страницу по адресу [url]
        """
        self.driver.get(url)
        time.sleep(2)
    
    def close_driver(self):
        """
            Закрывает браузер
        """
        self.driver.quit()

    def return_text_BY_CLASS_NAME(self, field: str):
        """
            возвращает текст елемента по имени класса
        """
        return self.driver.find_element(By.CLASS_NAME, field).text
    
    def wait_present_element_BY_CLASS_NAME(self, field:str):
        """
            Ожидает появление элемента на странице елемента по имени класса со значением 15
        """
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, field), "15"))

    def fill_element_BY_ID(self,id: str,str: str):
        """
            Заполняет значение элемента по имени id
        """
        delay = self.driver.find_element(By.ID,id)
        delay.clear()
        delay.send_keys(str)



    