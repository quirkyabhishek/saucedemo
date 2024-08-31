from selenium.webdriver.common.by import By
from utils.helper import wait_for_element, wait_for_element_to_be_clickable

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.zip_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.error_message_container = (By.CSS_SELECTOR, ".error-message-container")
    
    def enter_shipping_info(self, first_name, last_name, zip_code):
        wait_for_element(self.driver, By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
    
    def continue_checkout(self):
        wait_for_element_to_be_clickable(self.driver, By.ID, 'continue').click()

    def get_error_message(self):
        wait_for_element(self.driver, By.CSS_SELECTOR, ".error-message-container")
        return self.driver.find_element(*self.error_message_container).text