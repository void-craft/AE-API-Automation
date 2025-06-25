class TestLoginAPI:
    """Test cases for Login API"""
    
    def test_verify_login_valid_details(self, login_api, config, schema_validator):
        """Test API 7: POST To Verify Login with valid details"""
        response = login_api.verify_login(config.VALID_EMAIL, config.VALID_PASSWORD)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["responseCode"] == 200
        schema = schema_validator.get_login_success_schema()
        assert schema_validator.validate_response(response_json, schema)

    def test_verify_login_without_email(self, login_api, config, schema_validator):
        """Test API 8: POST To Verify Login without email parameter"""
        response = login_api.verify_login_without_email(config.VALID_PASSWORD)
        assert response.status_code == 200
        response_json = response.json()
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 400

    def test_delete_verify_login_method_not_allowed(self, login_api, schema_validator):
        """Test API 9: DELETE To Verify Login - Method Not Allowed"""
        response = login_api.delete_verify_login()
        assert response.status_code == 200
        response_json = response.json()
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 405

    def test_verify_login_invalid_details(self, login_api, config, schema_validator):
        """Test API 10: POST To Verify Login with invalid details"""
        response = login_api.verify_login_invalid(config.INVALID_EMAIL, config.INVALID_PASSWORD)
        assert response.status_code == 200
        response_json = response.json()
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 404