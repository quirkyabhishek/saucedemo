
# Sauce Demo Automation Framework

## Overview

This repository contains an automation framework for testing the [Sauce Demo](https://www.saucedemo.com/) web application. The framework is built using Python, Pytest, and Selenium. It is designed to automate testing scenarios for various functionalities of the Sauce Demo application.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
   - [Clone the Repository](#1-clone-the-repository)
   - [Create a Virtual Environment](#2-create-a-virtual-environment)
   - [Activate the Virtual Environment](#3-activate-the-virtual-environment)
   - [Install Dependencies](#4-install-dependencies)
3. [Usage](#usage)
   - [Writing Test Scripts](#1-writing-test-scripts)
   - [Utility Functions](#2-utility-functions)
4. [Project Structure](#project-structure)
5. [Running Tests](#running-tests)
6. [Additional Information](#additional-information)

## Requirements

- **Python**: Version 3.6 or above
- **Pytest**: Testing framework
- **Selenium**: Web automation library

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd sauce_demo_automation
```

Or just unzip the folder on your machine and:

```bash
cd sauce_demo_automation
```

### 2. Create a Virtual Environment

Create a virtual environment to manage project dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows (cmd)**:

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Writing Test Scripts

Test scripts are located in the `tests` directory. You can create or modify test scripts to cover different scenarios for the Sauce Demo application.

### 2. Utility Functions

Utility functions are located in the `utils` directory. These functions can be used across test scripts to avoid redundancy and improve maintainability.

## Project Structure

sauce_demo_automation/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── shopping_cart_page.py
│   ├── checkout_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_checkout.py
├── utils/
│   ├── __init__.py
│   ├── helper.py
├── screenshots/
├── conftest.py
├── requirements.txt
└── README.md

### Description

- **Test Automation Framework**:
  - **Page Object Model (POM)**: Contains page classes for interacting with different pages of the application. Each class encapsulates the elements and actions related to a specific page.
  - **Test Files**: Contains test files with parameterized test cases. Tests are designed to run in isolated browser instances to ensure test independence.
  - **Screenshot Handling**: Screenshots are saved in the `screenshots/` directory.
  - **Conftest Configuration**:
    - `conftest.py`: Sets up a new browser instance for each test function.
    - Creates the screenshots folder before test function if it doesn't exist.
    - Ensures proper cleanup of the WebDriver instance after each test.
  - **Utils**: Contains utility functions for common operations.
    - `helper.py`: Includes reusable functions like `screenshot()` and `wait_utils()`.

## Running Tests

To run the tests, ensure that the virtual environment is activated, and then execute the following command:

```bash
pytest
```

This will run all the test cases in the `tests` directory and display the results in the terminal.

## Additional Information

- **Headless Mode**: Tests are run in headless mode by default to avoid opening a browser window. If you prefer to see the browser, you can modify the `conftest.py` script to remove the `--headless` option from the `chrome_options`. (OR just comment that line)
  
- **Test Reports**: By default, Pytest outputs results to the terminal. For more detailed reporting, consider integrating with reporting tools like [pytest-html](https://pytest-html.readthedocs.io/en/latest/) or [pytest-cucumber](https://github.com/cucumber/pytest-cucumber).

- **Updating Dependencies**: If you need to add new packages, install them within the virtual environment and update the `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

- **Troubleshooting**: If you encounter issues, ensure that the virtual environment is active and dependencies are correctly installed. Check for specific error messages and refer to the [Selenium documentation](https://www.selenium.dev/documentation/en/) for troubleshooting tips.

For any questions or issues, please contact [abhishek.1si12ec004@gmail.com](mailto:abhishek.1si12ec004@gmail.com).