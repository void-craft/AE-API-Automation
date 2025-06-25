import pytest

class TestSearchAPI:
    """Test cases for Search API"""
    
    @pytest.mark.parametrize("search_term", ["top", "tshirt", "jean"])
    def test_search_product_success(self, search_api, schema_validator, search_term):
        """Test API 5: POST To Search Product - Success Cases"""
        response = search_api.search_product(search_term)
        assert response.status_code == 200
        response_json = response.json()
        assert "responseCode" in response_json
        assert "products" in response_json
        assert response_json["responseCode"] == 200
        schema = schema_validator.get_search_products_schema()
        assert schema_validator.validate_response(response_json, schema)

    def test_search_product_without_parameter(self, search_api, schema_validator):
        """Test API 6: POST To Search Product without search_product parameter"""
        response = search_api.search_product_without_param()
        assert response.status_code == 200
        response_json = response.json()
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 400