from wheel.signatures import assertTrue
from faker import Faker
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    f = Faker()

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
        check_login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assertTrue(check_login_form, f"{check_login_form} don't find on login page")

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        check_register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assertTrue(check_register_form, f"{check_register_form} don't find on login page")

    def register_new_user(self, email=f.name, password="12345678Jo"):
        self.fill_email_field(email)
        self.fill_pass1_field(password)
        self.fill_pass2_field(password)
        self.click_register_button()


    def fill_email_field(self, email):
        fill_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        fill_email.send_keys(email)

    def fill_pass1_field(self, password):
        fill_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_FIELD)
        fill_password1.send_keys(password)

    def fill_pass2_field(self, password):
        fill_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_FIELD)
        fill_password2.send_keys(password)

    def click_register_button(self):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
