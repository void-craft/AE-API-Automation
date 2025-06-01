from .base_api import BaseAPI
from typing import Dict

class UserAPI(BaseAPI):
    """User API service class"""
    
    def create_account(self, user_data: Dict):
        """Create/Register user account - API 11"""
        return self.post("createAccount", data=user_data)
    
    def delete_account(self, email: str, password: str):
        """Delete user account - API 12"""
        data = {'email': email, 'password': password}
        return self.delete("deleteAccount", data=data)
    
    def update_account(self, user_data: Dict):
        """Update user account - API 13"""
        return self.put("updateAccount", data=user_data)
    
    def get_user_detail_by_email(self, email: str):
        """Get user account detail by email - API 14"""
        params = {'email': email}
        return self.get("getUserDetailByEmail", params=params)