import pytest
from apis.products_api import ProductsAPI
from apis.brands_api import BrandsAPI
from apis.search_api import SearchAPI
from apis.login_api import LoginAPI
from apis.user_api import UserAPI
from utils.config import Config
from utils.schema_validator import SchemaValidator

# Validate environment configuration early
Config.validate_config()

@pytest.fixture(scope="session")
def config():
    """Configuration fixture"""
    return Config()

@pytest.fixture(scope="session")
def products_api():
    """Products API fixture"""
    api = ProductsAPI()
    yield api
    api.close()

@pytest.fixture(scope="session")
def brands_api():
    """Brands API fixture"""
    api = BrandsAPI()
    yield api
    api.close()

@pytest.fixture(scope="session")
def search_api():
    """Search API fixture"""
    api = SearchAPI()
    yield api
    api.close()

@pytest.fixture(scope="session")
def login_api():
    """Login API fixture"""
    api = LoginAPI()
    yield api
    api.close()

@pytest.fixture(scope="session")
def user_api():
    """User API fixture"""
    api = UserAPI()
    yield api
    api.close()

@pytest.fixture(scope="session")
def schema_validator():
    """Schema validator fixture"""
    return SchemaValidator()

@pytest.fixture
def test_user_data(config):
    """Test user data fixture"""
    return config.get_test_user_data()
