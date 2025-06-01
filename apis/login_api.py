from .base_api import BaseAPI
from typing import Optional

class LoginAPI(BaseAPI):
    """Login API service class"""
    
    def verify_login(self, email: Optional[str] = None, password: Optional[str] = None):
        """Verify login with email and password - API 7"""
        data = {}
        if email:
            data['email'] = email
        if password:
            data['password'] = password
        return self.post("verifyLogin", data=data)
    
    def verify_login_without_email(self, password: str):
        """Verify login without email parameter (should return 400) - API 8"""
        data = {'password': password}
        return self.post("verifyLogin", data=data)
    
    def delete_verify_login(self):
        """DELETE to verify login (should return 405) - API 9"""
        return self.delete("verifyLogin")
    
    def verify_login_invalid(self, email: str, password: str):
        """Verify login with invalid credentials (should return 404) - API 10"""
        data = {'email': email, 'password': password}
        return self.post("verifyLogin", data=data)