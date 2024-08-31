import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.helper import take_screenshot, get_current_time

@pytest.mark.parametrize("first_name, last_name, zip_code, expected_message", [
    ('Abhi', 'Shek', '12345', 'Thank you for your order!'),
    #('', 'Abhi', '12345', 'Error: First Name is required'),
    #('Abhi', '', '12345', 'Error: Last Name is required'),
    #('Abhi', 'Abhi', '', 'Error: Postal Code is required'),
    #('#', '-', '99999', 'Thank you for your order!')
])

def test_checkout_process(driver, first_name, last_name, zip_code, expected_message):

    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    
    product_page = ProductPage(driver)
    product_name = product_page.get_product_name(0)
    print(product_name)
    product_page.add_product_to_cart(0)
    product_page.go_to_cart()
    
    shopping_cart_page = ShoppingCartPage(driver)
    cart_product_name = shopping_cart_page.get_cart_product_name()
    print(cart_product_name)
    assert product_name == cart_product_name, "Product in cart does not match product added from product page"

    shopping_cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_shipping_info(first_name, last_name, zip_code)

    try:
        checkout_page.continue_checkout()
        checkout_step_two_page = CheckoutStepTwoPage(driver)
        checkout_step_two_page.complete_order()

        checkout_complete_page = CheckoutCompletePage(driver)
        confirmation_message = checkout_complete_page.get_confirmation_message()
        assert expected_message == confirmation_message
        take_screenshot(driver, f"screenshots/success_{get_current_time()}.png")

    except:
        error_message = checkout_page.get_error_message()
        assert expected_message == error_message
        take_screenshot(driver, f"screenshots/error_{get_current_time()}.png")