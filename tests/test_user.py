import pytest
import uuid

class TestUserAPI:
    """Test cases for User API"""
    
    def test_create_user_account_success(self, user_api, test_user_data, schema_validator):
        """Test API 11: POST To Create/Register User Account"""
        # Generate unique email to avoid conflicts
        test_user_data['email'] = f"test_{uuid.uuid4().hex[:8]}@example.com"
        
        response = user_api.create_account(test_user_data)
        
        # API returns 200 instead of 201
        assert response.status_code == 200
        response_json = response.json()
        
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 201
        assert "created" in response_json["message"].lower()
    
    def test_delete_user_account_success(self, user_api, schema_validator):
        """Test API 12: DELETE METHOD To Delete User Account"""
        # First create a user to delete
        test_data = {
            'name': 'Delete Test User',
            'email': f"delete_{uuid.uuid4().hex[:8]}@example.com",
            'password': 'deletetest123',
            'title': 'Mr',
            'birth_date': '15',
            'birth_month': '06',
            'birth_year': '1990',
            'firstname': 'Delete',
            'lastname': 'Test',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'address2': '',
            'country': 'United States',
            'zipcode': '12345',
            'state': 'California',
            'city': 'Test City',
            'mobile_number': '+1234567890'
        }
        
        # Create account - expect 200 instead of 201
        create_response = user_api.create_account(test_data)
        assert create_response.status_code == 200
        
        # Delete account
        delete_response = user_api.delete_account(test_data['email'], test_data['password'])
        
        assert delete_response.status_code == 200
        response_json = delete_response.json()
        
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 200
        assert "deleted" in response_json["message"].lower()
    
    def test_update_user_account_success(self, user_api, schema_validator):
        """Test API 13: PUT METHOD To Update User Account"""
        # First create a user to update
        test_data = {
            'name': 'Update Test User',
            'email': f"update_{uuid.uuid4().hex[:8]}@example.com",
            'password': 'updatetest123',
            'title': 'Mr',
            'birth_date': '15',
            'birth_month': '06',
            'birth_year': '1990',
            'firstname': 'Update',
            'lastname': 'Test',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'address2': '',
            'country': 'United States',
            'zipcode': '12345',
            'state': 'California',
            'city': 'Test City',
            'mobile_number': '+1234567890'
        }
        
        # Create account - expect 200 instead of 201
        create_response = user_api.create_account(test_data)
        assert create_response.status_code == 200
        
        # Update account
        test_data['name'] = 'Updated Test User'
        test_data['city'] = 'Updated City'
        update_response = user_api.update_account(test_data)
        
        assert update_response.status_code == 200
        response_json = update_response.json()
        
        schema = schema_validator.get_error_message_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 200
        assert "updated" in response_json["message"].lower()
    
    def test_get_user_detail_by_email_success(self, user_api, schema_validator):
        """Test API 14: GET user account detail by email"""
        # First create a user to retrieve
        test_data = {
            'name': 'Detail Test User',
            'email': f"detail_{uuid.uuid4().hex[:8]}@example.com",
            'password': 'detailtest123',
            'title': 'Ms',
            'birth_date': '20',
            'birth_month': '08',
            'birth_year': '1985',
            'firstname': 'Detail',
            'lastname': 'Test',
            'company': 'Detail Company',
            'address1': '456 Detail Street',
            'address2': 'Suite 789',
            'country': 'Canada',
            'zipcode': '54321',
            'state': 'Ontario',
            'city': 'Detail City',
            'mobile_number': '+1987654321'
        }
        
        # Create account - expect 200 instead of 201
        create_response = user_api.create_account(test_data)
        assert create_response.status_code == 200
        
        # Get user details
        detail_response = user_api.get_user_detail_by_email(test_data['email'])
        
        assert detail_response.status_code == 200
        response_json = detail_response.json()
        
        schema = schema_validator.get_user_detail_schema()
        assert schema_validator.validate_response(response_json, schema)
        assert response_json["responseCode"] == 200
        assert "user" in response_json
        
        # Verify user data matches
        user_data = response_json["user"]
        assert user_data["name"] == test_data["name"]
        assert user_data["email"] == test_data["email"]