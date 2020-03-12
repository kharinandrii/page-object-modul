from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id = 'login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id = 'register_form']")