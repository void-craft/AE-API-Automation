# API Automation Testing Project

This project is a Python-based API automation framework built to test the public APIs of automationexercise.com.
It uses PyTest for test execution, Requests for HTTP calls, and jsonschema for validating JSON responses.
The project follows a modular Service Object Model (SOM) architecture to keep tests clean, reusable, and maintainable.

## Project Structure
```bash
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
├── data/                      # Test data and JSON payloads
│   ├── login_data.json
│   └── user_data.json
├── utils/                     # Utility functions (e.g., JSON schema validator)
│   ├── schema_validator.py
│   ├── logger.py
│   └── config.py
├── conftest.py                # PyTest fixtures for setup like base URL, auth
├── requirements.txt           # Project dependencies: pytest, requests, jsonschema
├── .github/workflows/ci.yml   # GitHub Actions workflow to run tests on each push
└── README.md                  # Project overview and instructions
```

## Key Features So Far
Modular API service classes for separation of concerns

PyTest test cases with clear assertions and validations

JSON schema validation using jsonschema package

GitHub Actions configured for Continuous Integration (CI) to run tests automatically on code push

