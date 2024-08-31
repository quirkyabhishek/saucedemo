import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.helper import take_screenshot, get_current_time

@pytest.mark.parametrize("username, password, expected_title, expected_message", [
    ('standard_user', 'secret_sauce', 'Products', None),
    ('locked_out_user', 'secret_sauce', None, 'Epic sadface: Sorry, this user has been locked out.'),
    ('problem_user', 'secret_sauce', 'Products', None),
    ('performance_glitch_user', 'secret_sauce', 'Products', None),
    ('error_user', 'secret_sauce', 'Products', None),
    ('visual_user', 'secret_sauce', 'Products', None),
    ('standard_user', 'wrong_password', None, 'Epic sadface: Username and password do not match any user in this service'),
    ('', 'secret_sauce', None, 'Epic sadface: Username is required'),
    ('standard_user', '', None, 'Epic sadface: Password is required'),
    ('', '', None, 'Epic sadface: Username is required')
])

def test_login(driver, username, password, expected_title, expected_message):
    
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login(username, password)
    if expected_title:
        product_page = ProductPage(driver)
        assert product_page.get_title_text() == expected_title
        take_screenshot(driver, f"screenshots/success_{get_current_time()}.png")
        
    if expected_message:
        error_message = login_page.get_error_message()
        assert expected_message == error_message
        take_screenshot(driver, f"screenshots/error_{get_current_time()}.png")