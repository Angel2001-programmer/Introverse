import unittest
from test_api import TestAPI
from routes.user import check_email
from models.user_models import User


class TestUserAPI(TestAPI):
    """Tests for user namespace routes and related functions"""

    def test_valid_email(self):
        """Test a valid email address with check email"""
        result = check_email("test@email.com")
        self.assertTrue(result)

    def test_invalid_email(self):
        """Test an invalid email address with check email"""
        result = check_email("test.com")
        self.assertFalse(result)

    def test_register_successful(self):
        """Test successful registration of user"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code

        self.assertEqual(status_code, 201)

    def test_register_successful_max_length(self):
        """Test successful registration of user, username, first name and last name max characters"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "thisusernameisthirtycharacters",
                "first_name": "Iamexactlyfiftycharacterslongexactlyexactlyexactly",
                "last_name": "Iamexactlyfiftycharacterslongexactlyexactlyexactly",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code

        self.assertEqual(status_code, 201)

    def test_register_fail_invalid_email(self):
        """Test signing up with an invalid email address, unsuccessful registration"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code
        expected = {"error": "Email address is invalid"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_username_empty(self):
        """Test unsuccessful registration of user due to empty username"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code
        expected = {"error": "Username must be between 1 and 30 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_first_name_long(self):
        """Test unsuccessful registration of user due to too long first name"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "testtesttesttesttesttesttesttesttesttesttesttesttest",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code
        expected = {"error": "First name must be between 1 and 50 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_last_name_space(self):
        """Test unsuccessful registration of user due to empty last name, whitespace only"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "    ",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        status_code = register_response.status_code
        expected = {"error": "Last name must be between 1 and 50 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_username_conflict(self):
        """Test unsuccessful registration of user due to username already taken"""
        first_register = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        second_register = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "differentuser@test.com",
                "password": "mytestpassword"
            }
        )

        second_status_code = second_register.status_code
        expected = {"error": "Username is already taken"}
        result = second_register.json
        
        self.assertEqual(second_status_code, 409)
        self.assertEqual(expected, result)

    def test_register_fail_email_conflict(self):
        """Test unsuccessful registration of user due to email already taken"""
        first_register = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        second_register = self.client.post("/user/register",
            json = {
                "username": "differentuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        second_status_code = second_register.status_code
        expected = {"error": "Email is already registered"}
        result = second_register.json
        
        self.assertEqual(second_status_code, 409)
        self.assertEqual(expected, result)

    def test_login_successful(self):
        """Test creation of user and logging in successfully"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        login_response = self.client.post("/user/login",
            json = {
                "username": "testuser",
                "password": "mytestpassword"
            }
        )

        status_code = login_response.status_code
        json = login_response.json
        result = json["user"]
        expected = "testuser"

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_login_fail_incorrect_password(self):
        """Test creation of user and attempt of logging in with incorrect password"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        login_response = self.client.post("/user/login",
            json = {
                "username": "testuser",
                "password": "mywrongpassword"
            }
        )

        status_code = login_response.status_code
        expected = {"error": "Invalid credentials"}
        result = login_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_login_fail_no_username_exists(self):
        """Test creation of user and attempt of logging in with unregistered username"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        login_response = self.client.post("/user/login",
            json = {
                "username": "differentuser",
                "password": "mytestpassword"
            }
        )

        status_code = login_response.status_code
        expected = {"error": "Invalid credentials"}
        result = login_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()