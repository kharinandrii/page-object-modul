from selenium.webdriver.common.by import By

class MainPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    BOOK_NAME = (By.XPATH, "//div[@id = 'content_inner']//h1")
    BASKET_BUTTON = (By.XPATH, "//span[@class = 'btn-group']//a[contains(@class , 'btn btn-default')]")
    EMPTY_BASKET_TEXT =(By.XPATH, "//div[@id = 'content_inner']/p")