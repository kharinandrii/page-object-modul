from wheel.signatures import assertTrue

from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        check_url = self.browser.current_url
        assertTrue(check_url.endswith("/login/"), f"{check_url} don't contains /login/")

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        check_login_form = self.is_element_present(*MainPageLocators.LOGIN_FORM)
        assertTrue(check_login_form, f"{check_login_form} don't find on login page")

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        check_register_form = self.is_element_present(*MainPageLocators.REGISTER_FORM)
        assertTrue(check_register_form, f"{check_register_form} don't find on login page")

        # TODO разобраться с методом self.browser.current_url()

