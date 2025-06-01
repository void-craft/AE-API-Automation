import pytest
import json

class TestProductsAPI:
    """Test cases for Products API"""
    
    def test_get_all_products_success(self, products_api, schema_validator):
        """Test API 1: Get All Products List - Success Case"""
        response = products_api.get_all_products()
        
        # Verify status code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Verify response is JSON
        response_json = response.json()
        assert isinstance(response_json, dict), "Response should be JSON object"
        
        # Verify response structure
        assert "responseCode" in response_json, "Response should contain responseCode"
        assert "products" in response_json, "Response should contain products"
        assert response_json["responseCode"] == 200, "ResponseCode should be 200"
        
        # Verify products list is not empty
        assert len(response_json["products"]) > 0, "Products list should not be empty"
        
        # Validate schema
        schema = schema_validator.get_products_schema()
        assert schema_validator.validate_response(response_json, schema), "Response should match products schema"
    
    def test_post_to_products_list_method_not_allowed(self, products_api, schema_validator):
        """Test API 2: POST To All Products List - Method Not Allowed"""
        response = products_api.post_to_products_list()
        
        # Verify status code - API returns 200 instead of 405
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Verify response is JSON
        response_json = response.json()
        
        # Verify error message structure
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema), "Response should match error schema"
        
        # Verify error message content - responseCode should be 405
        assert response_json["responseCode"] == 405, "ResponseCode should be 405"