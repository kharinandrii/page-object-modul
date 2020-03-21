from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import pytest
from pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/"
link1 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    login_page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_lin(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link1)
    page.open()
    page.go_to_basket()
    page.check_price_product_in_empty_basket()
    page.check_empty_basket_text()
    page.text_for_empty_basket_is_present()
