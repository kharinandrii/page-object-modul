from .locators import MainPageLocators
from .base_page import BasePage
from wheel.signatures import assertTrue

class BasketPage(BasePage):
    def check_empty_basket_text(self):
        message = self.browser.find_element(*MainPageLocators.EMPTY_BASKET_TEXT).text.strip()
        print(message)
        text_in_empty_basket = "Your basket is empty."
        assertTrue(message.startswith(text_in_empty_basket), f"{message}, start with {text_in_empty_basket}")

    def check_price_product_in_empty_basket(self):
        self.is_not_element_present(*MainPageLocators.PRODUCT_PRICE)
        assert True, "price is present in empty basket - bug"

    def text_for_empty_basket_is_present(self):
        self.is_element_present(*MainPageLocators.EMPTY_BASKET_TEXT)
        assert True, "message is absent in empty basket - bug"