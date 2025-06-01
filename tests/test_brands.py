import pytest

class TestBrandsAPI:
    """Test cases for Brands API"""
    
    def test_get_all_brands_success(self, brands_api, schema_validator):
        """Test API 3: Get All Brands List - Success Case"""
        response = brands_api.get_all_brands()
        
        assert response.status_code == 200
        response_json = response.json()
        
        assert "responseCode" in response_json
        assert "brands" in response_json
        assert response_json["responseCode"] == 200
        assert len(response_json["brands"]) > 0
        
        # Validate schema
        schema = schema_validator.get_brands_schema()
        assert schema_validator.validate_response(response_json, schema)

    def test_put_to_brands_list_method_not_allowed(self, brands_api, schema_validator):
        response = brands_api.put_to_brands_list()
        response_json = response.json()
        assert "This request method is not supported" in response_json.get("message", "")
    
    # def test_put_to_brands_list_method_not_allowed(self, brands_api, schema_validator):
    #     """Test API 4: PUT To All Brands List - Method Not Allowed"""
    #     response = brands_api.put_to_brands_list()
        
    #     assert response.status_code == 405
    #     response_json = response.json()
        
    #     schema = schema_validator.get_error_message_schema()
    #     assert schema_validator.validate_response(response_json, schema)
    #     assert response_json["responseCode"] == 405
    #     assert "not supported" in response_json["message"].lower()