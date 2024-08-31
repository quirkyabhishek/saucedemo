import pytest
from selenium import webdriver
import os


@pytest.fixture()
def driver():
    # Setup WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode for CI/CD
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Ensure screenshots directory exists
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    
    yield driver  # Provide the driver to the test cases
    
    # Teardown WebDriver
    driver.quit()