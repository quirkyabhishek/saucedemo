from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def wait_for_element(driver, by, value, timeout=10):
    """
    Waits for an element to be present and visible on the page.
    :param driver: The WebDriver instance.
    :param by: The type of selector (e.g., By.CSS_SELECTOR).
    :param value: The selector value (e.g., '.my-class').
    :param timeout: Maximum time to wait in seconds.
    :return: The WebElement if found, else raises TimeoutException.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

def wait_for_element_to_be_clickable(driver, by, value, timeout=10):
    """
    Waits for an element to be clickable.
    :param driver: The WebDriver instance.
    :param by: The type of selector (e.g., By.CSS_SELECTOR).
    :param value: The selector value (e.g., '.my-button').
    :param timeout: Maximum time to wait in seconds.
    :return: The WebElement if clickable, else raises TimeoutException.
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

def wait_for_elements_to_be_clickable(driver, by, value, timeout=10):
    """
    Waits for a list of elements to be clickable.
    :param driver: The WebDriver instance.
    :param by: The type of selector (e.g., By.CSS_SELECTOR).
    :param value: The selector value (e.g., '.btn_inventory').
    :param timeout: Maximum time to wait in seconds.
    :return: List of WebElements if clickable, else raises TimeoutException.
    """
    elements = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_all_elements_located((by, value))
    )

def take_screenshot(driver, file_path):
    """
    Takes a screenshot of the current page and saves it to a file.
    :param driver: The WebDriver instance.
    :param file_path: Path where the screenshot will be saved.
    """
    driver.save_screenshot(file_path)

def get_current_time():
    """
    Returns the current time in a format suitable for file names.
    :return: Current time string.
    """
    return time.strftime("%Y%m%d-%H%M%S")
