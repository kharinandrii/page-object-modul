from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import  NoAlertPresentException
import math
import time
from wheel.signatures import assertTrue


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



    def check_first_message(self):
         first_message = self.browser.find_element(*MainPageLocators.MESSAGE_ADD_IN_BASKET).text
         TEXT_MESSAGE1 = "The shellcoder's handbook был добавлен в вашу корзину."
         assertTrue(first_message.startswith(TEXT_MESSAGE1), f"{first_message} don't start with {TEXT_MESSAGE1}")


    def check_second_message(self):
         second_message = self.browser.find_element(*MainPageLocators.BASKET_MESSAGE).text.strip()
         # time.sleep(3600)
         print(second_message)
         TEXT_MESSAGE1 = "Ваша корзина удовлетворяет условиям предложения Deferred benefit offer."
         print(TEXT_MESSAGE1)
         assertTrue(second_message.endswith(TEXT_MESSAGE1), f"{second_message} don't finish with {TEXT_MESSAGE1}")


    def check_cost(self):
        cost_message = self.browser.find_element(*MainPageLocators.BASKET_COST).text
        check_product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text
        assertTrue(cost_message == check_product_price, f"{cost_message} don't equals {check_product_price}")
