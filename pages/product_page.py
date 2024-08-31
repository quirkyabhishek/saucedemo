from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import wait_for_element, wait_for_elements_to_be_clickable

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.product_name = (By.CSS_SELECTOR, ".inventory_item_name")
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
    
    def add_product_to_cart(self, index):
        buttons = wait_for_elements_to_be_clickable(self.driver, By.CLASS_NAME, "btn_inventory")
        buttons[index].click()

    def get_title_text(self):
        title_element = wait_for_element(self.driver, By.CLASS_NAME, 'title')
        return title_element.text
    
    def get_product_name(self, index):
        # Assuming index is used to select a specific product if multiple products are present
        product_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.product_name)
        )
        return product_elements[index].text