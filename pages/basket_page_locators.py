from selenium.webdriver.common.by import By

class BasketPageLocators():
    MESSAGE_ADD_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div")
    BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']/div[2]/div")
    BASKET_COST = (By.XPATH,"//div[@id='messages']/div[3]/div/p[1]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    BOOK_NAME = (By.XPATH, "//div[@id = 'content_inner']//h1")