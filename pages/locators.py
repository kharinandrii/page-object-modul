from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    BOOK_NAME = (By.XPATH, "//div[@id = 'content_inner']//h1")
    BASKET_BUTTON = (By.XPATH, "//span[@class = 'btn-group']//a[contains(@class , 'btn btn-default')]")
    EMPTY_BASKET_TEXT =(By.XPATH, "//div[@id = 'content_inner']/p")

class BasketPageLocators:
    MESSAGE_ADD_IN_BASKET = (By.XPATH, "//div[@class = 'page_inner']/div[@id='messages']/div[1]/div")
    BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']/div[2]/div")
    BASKET_COST = (By.XPATH,"//div[@id='messages']/div[3]/div/p[1]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    BOOK_NAME = (By.XPATH, "//div[@id = 'content_inner']//h1")

class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id = 'login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id = 'register_form']")
    REGISTER_EMAIL_FIELD = (By.XPATH,"//input[@id = 'id_registration-email']")
    REGISTER_PASSWORD1_FIELD = (By.XPATH, "//input[@id = 'id_registration-password1']")
    REGISTER_PASSWORD2_FIELD = (By.XPATH, "//input[@id = 'id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name = 'registration_submit' ]")

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")