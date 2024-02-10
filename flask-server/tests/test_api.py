import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig

class APITestCase(TestCase):
    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app=create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():

            db.create_all()

    def test_hello_world(self):
        """Test the hello world route"""
        hello_response = self.client.get("/content/hello")
        result = hello_response.json
        expected = {"message": "Hello world!"}
        # print(result)

        self.assertEqual(expected, result)

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
        print(json)

        self.assertEqual(status_code, 401)

    def test_get_all_posts(self):
        """Test getting all forum posts"""
        forum_response = self.client.get("/forum/all")

        status_code = forum_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_post_id_not_found(self):
        """Test get post by id route, with no data"""
        id=1
        response = self.client.get(f"/forum/id/{id}")
        status_code = response.status_code

        self.assertEqual(status_code, 404)

    def test_create_post_successful(self):
        """Test creating a post, login required for @jwt_required route"""
        register_response = self.client.post("/user/register",
            json = {
                "username": "testuser",
                "first_name": "test",
                "last_name": "user",
                "email": "testuser@test.com",
                "password": "mytestpassword"
            }
        )

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("forum/all",
            json = {
                "post_content": "Test content",
                "post_category": "Test",
                "post_author": "testuser"
            },
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = create_post_response.status_code

        self.assertEqual(status_code, 201)

    
    def test_create_post_unsuccessful(self):
        """Test creating a post without access token"""
        create_post_response = self.client.post("forum/all",
            json = {
                "post_content": "Test content",
                "post_category": "Test",
                "post_author": "testuser"
            }
        )

        status_code = create_post_response.status_code

        self.assertEqual(status_code, 401)


    def test_edit_post(self):
        pass

    def test_delete_post(self):
        pass
    

    def tearDown(self):
        """Destroy all the instances created for testing, remove sessions and drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()