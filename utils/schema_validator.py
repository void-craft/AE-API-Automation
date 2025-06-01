import jsonschema
from jsonschema import validate

class SchemaValidator:
    """Schema validator for API responses"""
    
    def validate_response(self, response_data, schema):
        """Validate response against schema"""
        try:
            validate(instance=response_data, schema=schema)
            return True
        except jsonschema.exceptions.ValidationError:
            return False
    
    def get_error_message_schema(self):
        """Schema for error responses"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "message": {"type": "string"}
            },
            "required": ["responseCode", "message"]
        }
    
    def get_login_success_schema(self):
        """Schema for successful login response"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "message": {"type": "string"}
            },
            "required": ["responseCode", "message"]
        }
    
    def get_search_products_schema(self):
        """Schema for search products response"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "price": {"type": "string"},
                            "brand": {"type": "string"},
                            "category": {
                                "type": "object",
                                "properties": {
                                    "usertype": {
                                        "type": "object",
                                        "properties": {
                                            "usertype": {"type": "string"}
                                        }
                                    },
                                    "category": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            },
            "required": ["responseCode", "products"]
        }
    
    def get_brands_schema(self):
        """Schema for brands list response"""
        return {
            "type": "object", 
            "properties": {
                "responseCode": {"type": "integer"},
                "brands": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "brand": {"type": "string"}
                        },
                        "required": ["id", "brand"]
                    }
                }
            },
            "required": ["responseCode", "brands"]
        }
    
    def get_products_schema(self):
        """Schema for products list response"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "price": {"type": "string"},
                            "brand": {"type": "string"},
                            "category": {"type": "object"}
                        }
                    }
                }
            },
            "required": ["responseCode", "products"]
        }
    
    def get_user_creation_schema(self):
        """Schema for user creation response"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "message": {"type": "string"}
            },
            "required": ["responseCode", "message"]
        }
    
    def get_user_detail_schema(self):
        """Schema for user detail response"""
        return {
            "type": "object",
            "properties": {
                "responseCode": {"type": "integer"},
                "user": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "title": {"type": "string"},
                        "birth_date": {"type": "string"},
                        "birth_month": {"type": "string"},
                        "birth_year": {"type": "string"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "company": {"type": "string"},
                        "address1": {"type": "string"},
                        "address2": {"type": "string"},
                        "country": {"type": "string"},
                        "zipcode": {"type": "string"},
                        "state": {"type": "string"},
                        "city": {"type": "string"},
                        "mobile_number": {"type": "string"}
                    }
                }
            },
            "required": ["responseCode", "user"]
        }