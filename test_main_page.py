from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    login_page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page.should_be_login_page()



def test_guest_should_see_login_lin(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


