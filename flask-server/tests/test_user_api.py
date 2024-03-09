import unittest
from test_api import TestAPI, create_user_json, default_user
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
        register_response = self.client.post("/user/register", json=default_user)

        status_code = register_response.status_code

        self.assertEqual(status_code, 201)

    def test_register_successful_max_length(self):
        """Test successful registration of user, username, first name and last name max characters"""
        register_response = self.client.post("/user/register",
            json=create_user_json("thisusernameisthirtycharacters",
                                  "Iamexactlyfiftycharacterslongexactlyexactlyexactly",
                                    "Iamexactlyfiftycharacterslongexactlyexactlyexactly",
                                  "testuser@test.com", "mytestpassword")
        )

        status_code = register_response.status_code

        self.assertEqual(status_code, 201)

    def test_register_fail_invalid_email(self):
        """Test signing up with an invalid email address, unsuccessful registration"""
        register_response = self.client.post("/user/register",
            json=create_user_json(email="testuser@test")
        )

        status_code = register_response.status_code
        expected = {"message": "Email address is invalid"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_username_empty(self):
        """Test unsuccessful registration of user due to empty username"""
        register_response = self.client.post("/user/register",
            json=create_user_json(username="")
        )

        status_code = register_response.status_code
        expected = {"message": "Username must be between 1 and 30 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_first_name_long(self):
        """Test unsuccessful registration of user due to too long first name"""
        register_response = self.client.post("/user/register",
            json=create_user_json(first_name="testtesttesttesttesttesttesttesttesttesttesttesttest")
        )

        status_code = register_response.status_code
        expected = {"message": "First name must be between 1 and 50 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_last_name_space(self):
        """Test unsuccessful registration of user due to empty last name, whitespace only"""
        register_response = self.client.post("/user/register",
            json=create_user_json(last_name="    ")
        )

        status_code = register_response.status_code
        expected = {"message": "Last name must be between 1 and 50 characters"}
        result = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_register_fail_username_conflict(self):
        """Test unsuccessful registration of user due to username already taken"""
        first_register = self.client.post("/user/register", json=default_user)

        second_register = self.client.post("/user/register",
            json=create_user_json(email="differentuser@test.com")
        )

        second_status_code = second_register.status_code
        expected = {"message": "Username is already taken"}
        result = second_register.json
        
        self.assertEqual(second_status_code, 409)
        self.assertEqual(expected, result)

    def test_register_fail_email_conflict(self):
        """Test unsuccessful registration of user due to email already taken"""
        first_register = self.client.post("/user/register", json=default_user)

        second_register = self.client.post("/user/register",
            json=create_user_json(username="differentuser")
        )

        second_status_code = second_register.status_code
        expected = {"message": "Email is already registered"}
        result = second_register.json
        
        self.assertEqual(second_status_code, 409)
        self.assertEqual(expected, result)

    def test_login_successful(self):
        """Test creation of user and logging in successfully"""
        register_response = self.client.post("/user/register", json=default_user)

        login_response = self.client.post("/user/login",
            json={
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
        register_response = self.client.post("/user/register", json=default_user)

        login_response = self.client.post("/user/login",
            json={
                "username": "testuser",
                "password": "mywrongpassword"
            }
        )

        status_code = login_response.status_code
        expected = {"message": "Invalid credentials"}
        result = login_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_login_fail_no_username_exists(self):
        """Test creation of user and attempt of logging in with unregistered username"""
        register_response = self.client.post("/user/register", json=default_user)

        login_response = self.client.post("/user/login",
            json={
                "username": "differentuser",
                "password": "mytestpassword"
            }
        )

        status_code = login_response.status_code
        expected = {"message": "Invalid credentials"}
        result = login_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)


    def test_get_profile_successful(self):
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        get_response = self.client.get(f"/user/current_user",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        result = get_response.json
        print(result)

# TODO: Test other routes - logout, members etc

if __name__ == "__main__":
    unittest.main()
