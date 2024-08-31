from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, 'finish')
    
    def complete_order(self):
        self.driver.find_element(*self.finish_button).click()