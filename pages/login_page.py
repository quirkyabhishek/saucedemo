from selenium.webdriver.common.by import By
from utils.helper import wait_for_element

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.error_message_container = (By.CSS_SELECTOR, ".error-message-container")
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        wait_for_element(self.driver, By.CSS_SELECTOR, ".error-message-container")
        return self.driver.find_element(*self.error_message_container).text