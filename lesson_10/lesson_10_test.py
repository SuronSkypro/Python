from  lesson_10_1_mainpage import MainPage
from lesson_10_3_shop import ShopPage
from lesson_10_2_calc import CalcPage
import allure

username = "standard_user"
password = "secret_sauce"

@allure.title("Тест магазина")
@allure.description("Тест магазина")
@allure.feature("Test")
@allure.severity("BLOCKER")
@allure.story("Тест магазина")
def test_Shop():

    with allure.step("Открываем страницу магазина"):
        TestPage = ShopPage(browser='chrome')
        TestPage.open_url("https://www.saucedemo.com/")

    with allure.step("Авторизируемся"):
        TestPage.autorize(username,password)
    
    with allure.step("Добавляем товар в корзину"):
        TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-backpack")
        TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-bolt-t-shirt")
        TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-onesie")
    
    with allure.step("Переходми в корзину"):
        TestPage.click_cart()

    with allure.step("Покупаем"):
        TestPage.click_button_BY_ID("checkout")
    
        TestPage.fill_field_BY_ID("first-name", "Александр")
        TestPage.fill_field_BY_ID("last-name", "Недоростков")
        TestPage.fill_field_BY_ID("postal-code", "440028")

        TestPage.click_button_BY_ID("continue")

    with allure.step("Проверяем сумму покупки"):
        total_amount =  TestPage.return_text_BY_CLASS_NAME("summary_total_label")
        assert total_amount == "Total: $58.29"

    TestPage.close_driver()

@allure.title("Тест главной страницы")
@allure.description("Тест главной страницы")
@allure.feature("Test")
@allure.severity("BLOCKER")
@allure.story("Тест главной страницы")
def test_lesson_10_1():

    with allure.step("Открываем страницу"):
        TestPage = MainPage(browser='chrome')
        TestPage.open_url('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    
    with allure.step("Заполняем поля"):
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

    with allure.step("Проверяем элементы на соответствие нужному цвету"):
        text_color =  TestPage.zipcode_color()
        assert text_color == "rgba(132, 32, 41, 1)"
        print("Цвет zip красный:", text_color)


        alert_elements = TestPage.find_elements(".alert.py-2.alert-success")
        assert len(alert_elements) == 9 

        for idx, element in enumerate(alert_elements):
            el_color = alert_elements[idx].value_of_css_property("color")
            assert el_color == "rgba(15, 81, 50, 1)"
            print ("Ok")

    
    TestPage.close_driver()

@allure.title("Тест калькулятора")
@allure.description("Тест калькулятора")
@allure.feature("Test")
@allure.severity("BLOCKER")
@allure.story("Тест калькулятора")
def test_calc():

    TestPage = CalcPage(browser='chrome')

    TestPage.open_url("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    TestPage.fill_element_BY_ID("delay","45")
        
    TestPage.press_button_BY_XPATH("//span[text()='7']")
    TestPage.press_button_BY_XPATH("//span[text()='+']")
    TestPage.press_button_BY_XPATH("//span[text()='8']")
    TestPage.press_button_BY_XPATH("//span[text()='=']")
       
    #TestPage.wait_present_element_BY_CLASS_NAME("screen")
    
    result = TestPage.return_text_BY_CLASS_NAME("screen")
    assert result == "15"
       
    TestPage.close_driver()

