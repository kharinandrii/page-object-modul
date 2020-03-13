from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link1 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link1)
    product_page = ProductPage(browser, link1)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_first_message()
    product_page.check_second_message()
    product_page.check_cost()