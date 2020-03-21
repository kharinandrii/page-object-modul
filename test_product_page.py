import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage



@pytest.mark.parametrize(
    'link1', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link1):
    browser.get(link1)
    product_page = ProductPage(browser, link1)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_first_message()
    product_page.check_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link1)
    product_page = ProductPage(browser, link1)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    browser.get(link1)
    product_page = ProductPage(browser, link1)
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link1)
    product_page = ProductPage(browser, link1)
    product_page.add_to_basket()
    product_page.message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link1 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link1)
    page.open()
    page.go_to_basket()
    page.check_empty_basket_text()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setUp(self, browser):
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
        login_page = LoginPage(browser, link1)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user()
        page = BasePage(browser, link1)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
        product_page = ProductPage(browser, link1)
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
        browser.get(link1)
        product_page = ProductPage(browser, link1)
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_first_message()
        product_page.check_cost()

