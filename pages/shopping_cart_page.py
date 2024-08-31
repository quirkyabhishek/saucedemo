from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')
        self.cart_product_name = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    
    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_product_name)
        ).text