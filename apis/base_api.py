import requests
from typing import Dict, Optional
import logging

class BaseAPI:
    """Base API class with common HTTP methods and utilities"""
    
    def __init__(self, base_url: str = "https://automationexercise.com/api"):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
    
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make GET request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"GET {url} with params: {params}")
        response = self.session.get(url, params=params, **kwargs)
        self.logger.info(f"Response: {response.status_code}")
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"POST {url} with data: {data or json}")
        response = self.session.post(url, data=data, json=json, **kwargs)
        self.logger.info(f"Response: {response.status_code}")
        self.logger.info(f"Response body: {response.text}")  # Add this line
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make PUT request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"PUT {url} with data: {data or json}")
        response = self.session.put(url, data=data, json=json, **kwargs)
        self.logger.info(f"Response: {response.status_code}")
        return response
    
    def delete(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make DELETE request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"DELETE {url} with data: {data}")
        response = self.session.delete(url, data=data, **kwargs)
        self.logger.info(f"Response: {response.status_code}")
        return response
    
    def close(self):
        """Close the session"""
        self.session.close()