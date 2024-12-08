from lesson_7_2_calc import CalcPage

def test_calc():

    TestPage = CalcPage(browser='chrome')

    TestPage.open_url("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    TestPage.fill_element_BY_ID("delay","45")
        
    TestPage.press_button_BY_XPATH("//span[text()='7']")
    TestPage.press_button_BY_XPATH("//span[text()='+']")
    TestPage.press_button_BY_XPATH("//span[text()='8']")
    TestPage.press_button_BY_XPATH("//span[text()='=']")
       
    TestPage.wait_present_element_BY_CLASS_NAME("screen")
    
    result = TestPage.return_text_BY_CLASS_NAME("screen")
    assert result == "15"
       
    TestPage.close_driver()
