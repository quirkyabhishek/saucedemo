from selenium.webdriver.common.by import By
from utils.helper import wait_for_element

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_message = (By.CLASS_NAME, 'complete-header')
    
    def get_confirmation_message(self):
        wait_for_element(self.driver, By.CLASS_NAME, 'complete-header')
        return self.driver.find_element(*self.confirmation_message).text