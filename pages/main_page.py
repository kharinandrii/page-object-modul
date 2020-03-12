from selenium.webdriver.common.by import By
from wheel.signatures import assertTrue

from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        check_login_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assertTrue(check_login_link, f"{check_login_link} don't find on login page")

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not presented"