import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig

class TestForumAPI(TestCase):
    """Tests for forum namespace routes"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app=create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():

            db.create_all()

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