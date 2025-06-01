from .base_api import BaseAPI
from typing import Optional

class SearchAPI(BaseAPI):
    """Search API service class"""
    
    def search_product(self, search_term: Optional[str] = None):
        """Search for products - API 5"""
        data = {}
        if search_term:
            data['search_product'] = search_term
        return self.post("searchProduct", data=data)
    
    def search_product_without_param(self):
        """Search without search_product parameter (should return 400) - API 6"""
        return self.post("searchProduct")