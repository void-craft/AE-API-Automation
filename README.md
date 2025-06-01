# API Automation Testing Project
A comprehensive Python-based API automation framework for testing automationexercise.com APIs using PyTest, Requests, and JSON Schema validation.

## Features
- Service Object Model (SOM): Clean separation of API calls from test logic
- Comprehensive Test Coverage: 14 different API endpoints with positive/negative scenarios
- JSON Schema Validation: Automatic response structure validation
- CI/CD Integration: GitHub Actions workflow for automated testing
- Detailed Logging: Request/response logging with timestamps
- Parameterized Testing: Data-driven tests using PyTest parameters
- Allure Reports: Generate detailed reports on local and CI using GitHub Actions

## Project Structure
```
api-automation-project/
├── apis/                      # API service classes handling HTTP requests
│   ├── products_api.py
│   ├── brands_api.py
│   ├── search_api.py
│   ├── login_api.py
│   ├── user_api.py
│   └── base_api.py
├── tests/                     # PyTest test cases for different API modules
│   ├── test_products.py
│   ├── test_brands.py
│   ├── test_search.py
│   ├── test_login.py
│   └── test_user.py
├── utils/                     # Utility functions (e.g., JSON schema validator)
│   ├── schema_validator.py
│   ├── logger.py
│   └── config.py
├── conftest.py                # PyTest fixtures for setup like base URL, auth
├── requirements.txt           # Project dependencies: pytest, requests, jsonschema
├── .github/workflows/ci.yml   # GitHub Actions workflow to run tests on each push
└── README.md                  # Project overview and instructions
```

## API Test Coverage

API Endpoint, Method, Expected-Status, Test-Type

 - 1/productsListGET200Positive
 - 2/productsListPOST405Negative
 - 3/brandsListGET200Positive
 - 4/brandsListPUT405Negative
 - 5/searchProductPOST200Positive
 - 6/searchProductPOST400Negative
 - 7/verifyLoginPOST200Positive
 - 8/verifyLoginPOST400Negative
 - 9/verifyLoginDELETE405Negative
 - 10/verifyLoginPOST404Negative
 - 11/createAccountPOST201Positive
 - 12/deleteAccountDELETE200Positive
 - 13/updateAccountPUT200Positive
 - 14/getUserDetailByEmailGET200Positive

## Installation

```
git clone <repository-url>
cd api-automation-project
pip install -r requirements.txt
```

## Running Tests

### Run all tests
```
pytest tests/ -v
```

### Run specific test file
```
pytest tests/test_products.py -v
```

### Run in parallel
```
pytest tests/ -n auto
```

## Allure Reports
To install Allure CLI locally (Windows):

### Install Scoop:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
iwr -useb get.scoop.sh | iex
scoop install allure

### Generate Allure report locally:
pytest --alluredir=allure-results
allure serve allure-results

- Allure CI Integration is configured in .github/workflows/ci.yml


## Test Structure

API Services (apis/)

- base_api.py: Base class with common HTTP methods
- products_api.py: Products-related API calls
- brands_api.py: Brands-related API calls
- search_api.py: Search functionality
- login_api.py: Authentication endpoints
- user_api.py: User management operations

Test Files (tests/)

- test_products.py: Product API tests
- test_brands.py: Brand API tests
- test_search.py: Search API tests
- test_login.py: Login API tests
- test_user.py: User management tests

Utilities (utils/)

- schema_validator.py: JSON schema validation
- config.py: Configuration management
- logger.py: Logging utilities

Key Testing Concepts

- Positive Testing: Valid requests returning expected successful responses
- Negative Testing: Invalid requests returning appropriate error codes
- Method Validation: Unsupported HTTP methods return 405 errors
- Parameter Validation: Missing parameters return 400 errors
- Schema Validation: Response structure matches expected JSON schemas

## CI/CD Pipeline

GitHub Actions automatically runs tests on:
- Push to main/develop branches
- Pull requests to main branch
- Multiple Python versions (3.8, 3.9, 3.10)

## Configuration

Update utils/config.py to modify:
- Base URL
- Timeout settings
- Test data

Update .env to modify:
- Test credentials in local

And in Github Actions > Secrets to modify:
- Test credentials in CI

## Reports

Tests generate Allure reports showing:
- Pass/fail status
- Request/response details
- Assertion failures
