from  lesson_7_1_mainpage import MainPage
 


def test_lesson_7_1():

    TestPage = MainPage(browser='chrome')
    TestPage.open_url('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    TestPage.fill_field("first-name","Петя")
    TestPage.fill_field("last-name","Петя")
    TestPage.fill_field("first-name","Петров")
    TestPage.fill_field("address","Ленина, 55-3")
    TestPage.fill_field("zip-code","")
    TestPage.fill_field("e-mail","test@skypro.com")
    TestPage.fill_field("phone","+7985899998787")
    TestPage.fill_field("city","Москва")
    TestPage.fill_field("country","Россия")
    TestPage.fill_field("job-position","QA")
    TestPage.fill_field("company","SkyPro")

    TestPage.press_button("//button[text()='Submit']")
    # Проверка цветов

    text_color =  TestPage.zipcode_color()
    assert text_color == "rgba(132, 32, 41, 1)"
    print("Цвет zip красный:", text_color)


    alert_elements = TestPage.find_elements(".alert.py-2.alert-success")

    for idx, element in enumerate(alert_elements):
        el_color = alert_elements[idx].value_of_css_property("color")
        assert el_color == "rgba(15, 81, 50, 1)"
        print ("Ok")

    
    TestPage.close_driver()

