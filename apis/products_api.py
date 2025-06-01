from .base_api import BaseAPI

class ProductsAPI(BaseAPI):
    """Products API service class"""
    
    def get_all_products(self):
        """Get all products list - API 1"""
        return self.get("productsList")
    
    def post_to_products_list(self):
        """POST to products list (should return 405) - API 2"""
        return self.post("productsList")