# Automation Testing with Python, Pytest, and Page Object Model (POM)

This repository contains an example project demonstrating automation testing of the Swag Labs website using Python, Pytest, and the Page Object Model (POM) design pattern.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of this project is to showcase how to perform automation testing for the Swag Labs website using Python as the programming language, Pytest as the testing framework, and the Page Object Model (POM) as the design pattern.

The Swag Labs website is an e-commerce platform that sells various products. This project demonstrates how to automate the testing of the website's functionality, such as user login, product browsing, cart management, and checkout process.

## Project Structure

The project has the following structure:

```
.
├── tests
│   ├── pages
│   │   ├── base_page.py
│   │   ├── cart_page.py
│   │   ├── login_page.py
│   │   └── product_page.py
│   ├── tests
│   │   ├── test_login.py
│   │   ├── test_product_browsing.py
│   │   ├── test_cart_management.py
│   │   └── test_checkout_process.py
│   └── conftest.py
├── utils
│   └── data.py
├── .gitignore
├── README.md
└── requirements.txt
```

- The `tests` directory contains the test files organized by functionality. Each test file focuses on a specific aspect of the website and imports the necessary page objects.
- The `pages` directory contains the page object files that encapsulate the website's different pages and their associated actions and elements.
- The `conftest.py` file contains configuration and fixtures used by the test files.
- The `utils` directory contains utility files that assist in the testing process, such as generating test data.
- The `.gitignore` file specifies which files and directories should be ignored by version control.
- The `README.md` file (this file) provides an overview of the project and instructions for running the tests.
- The `requirements.txt` file lists the Python dependencies required to run the tests.

## Installation

To install the necessary dependencies for running the tests, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Abhi147369/AutomationTesting-SwagLabs.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AutomationTesting-SwagLabs
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

To run the tests, ensure that you have completed the installation steps mentioned above.

1. Activate the virtual environment (if not already activated):

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

2. Run the tests using the

 following command:

   ```bash
   pytest
   ```

   This command will discover and execute all the test files within the `tests` directory.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

When contributing, please ensure that you follow appropriate coding conventions, write clear commit messages, and provide a detailed description of the changes you have made.

## License

This project is prepared by ABHISHEK GAVKARE.
