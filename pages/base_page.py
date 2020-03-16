from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import MainPageLocators
from wheel.signatures import assertTrue


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)

    def is_element_present(self,type_locator, element):
        try:
            self.browser.find_element(type_locator, element)
        except NoSuchElementException as e :
            return False
        return True

    def is_not_element_present(self, type_locator, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((type_locator, element)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, type_locator, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((type_locator, element)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        check_login_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assertTrue(check_login_link, f"{check_login_link} don't find on login page")

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not presented"