from lesson_7_2_shop import ShopPage

username = "standard_user"
password = "secret_sauce"

def test_Shop():

    TestPage = ShopPage(browser='chrome')

    TestPage.open_url("https://www.saucedemo.com/")

    TestPage.autorize(username,password)
    
    TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-backpack")
    TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-bolt-t-shirt")
    TestPage.add_item_to_cart_BY_ID("add-to-cart-sauce-labs-onesie")
    
    TestPage.click_cart()

    TestPage.click_button_BY_ID("checkout")
    
    TestPage.fill_field_BY_ID("first-name", "Александр")
    TestPage.fill_field_BY_ID("last-name", "Недоростков")
    TestPage.fill_field_BY_ID("postal-code", "440028")

    TestPage.click_button_BY_ID("continue")

       
    total_amount =  TestPage.return_text_BY_CLASS_NAME("summary_total_label")
    assert total_amount == "Total: $58.29"

    TestPage.close_driver()


