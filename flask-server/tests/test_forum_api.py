import unittest
from test_api import TestAPI


class TestForumAPI(TestAPI):
    """Tests for forum namespace routes"""

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

    
    def test_create_post_fail_no_access_token(self):
        """Test creating a post without access token"""
        create_post_response = self.client.post("forum/all",
            json = {
                "post_content": "Test content",
                "post_category": "Test",
                "post_author": "testuser"
            }
        )

        status_code = create_post_response.status_code
        expected = {'error': 'authorisation_token', 'message': 'Request does not contain a valid token'}
        result = create_post_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_create_post_fail_invalid_token(self):
        """Test creating a post, invalid access token"""
        invalid_token = "invalidtoken"

        create_post_response = self.client.post("forum/all",
            json = {
                "post_content": "Test content",
                "post_category": "Test",
                "post_author": "testuser"
            },
            headers = {
                "Authorization": f"Bearer {invalid_token}"
            }
        )

        status_code = create_post_response.status_code
        expected = {'error': 'invalid_token', 'message': 'Signature verification failed'}
        result = create_post_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)


    def test_edit_post(self):
        """Test editing a post, login required for @jwt_required route"""
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

    def test_delete_post(self):
        pass


if __name__ == "__main__":
    unittest.main()