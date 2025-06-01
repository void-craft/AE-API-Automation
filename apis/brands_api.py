from .base_api import BaseAPI

class BrandsAPI(BaseAPI):
    """Brands API service class"""
    
    def get_all_brands(self):
        """Get all brands list - API 3"""
        return self.get("brandsList")
    
    def put_to_brands_list(self):
        """PUT to brands list (should return 405) - API 4"""
        return self.put("brandsList")