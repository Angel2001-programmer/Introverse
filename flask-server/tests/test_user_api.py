import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig
from routes.user import user_access_tokens, check_email

class TestUserAPI(TestCase):
    """Tests for user namespace routes and related functions"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app=create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():

            db.create_all()

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

    def test_register_invalid_email(self):
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

        self.assertEqual(status_code, 400)

    def test_register_username_empty(self):
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
        json = register_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, json)


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
        # print(json)

        self.assertEqual(status_code, 200)

    def test_login_invalid_credentials(self):
        """Test creation of user and attempt of logging in with incorrect credentials"""
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
        json = login_response.json
        # print(json)

        self.assertEqual(status_code, 401)

    def tearDown(self):
        """Destroy all the instances created for testing, remove sessions and drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()