import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for API testing"""
    
    BASE_URL = "https://automationexercise.com/api"
    VALID_EMAIL = os.getenv('TEST_EMAIL')
    VALID_PASSWORD = os.getenv('TEST_PASSWORD')
    INVALID_EMAIL = os.getenv('INVALID_TEST_EMAIL', 'invalid@example.com')
    INVALID_PASSWORD = os.getenv('INVALID_TEST_PASSWORD', 'wrongpassword')
    REQUEST_TIMEOUT = 30
    DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
    
    @classmethod
    def get_test_user_data(cls):
        """Get complete user data for account creation"""
        return {
            'name': 'Test User',
            'email': cls.VALID_EMAIL,
            'password': cls.VALID_PASSWORD,
            'title': 'Mrs',
            'birth_date': '01',
            'birth_month': '01',
            'birth_year': '2000',
            'firstname': 'Test',
            'lastname': 'User',
            'company': 'Test Company',
            'address1': 'Test Address',
            'address2': '',
            'country': 'India',
            'zipcode': '600060',
            'state': 'Tamil Nadu',
            'city': 'Chennai',
            'mobile_number': '1111111111'
        }
    
    @classmethod
    def validate_config(cls):
        """Validate required environment variables are set"""
        if not cls.VALID_EMAIL or not cls.VALID_PASSWORD:
            raise ValueError("TEST_EMAIL and TEST_PASSWORD environment variables must be set")