import unittest
from test_auth_api import TestAPI, create_user_json, default_user


def create_post_json(post_content="Test content", post_category="Test", post_author="testuser"):
    """Function to create post json"""
    json = {
                "post_content": post_content,
                "post_category": post_category,
                "post_author": post_author
            }
    return json


example_post = create_post_json()


class TestForumAPI(TestAPI):
    """Tests for forum namespace routes"""

    def test_get_all_posts(self):
        """Test getting all forum posts"""
        forum_response = self.client.get("/forum/all")

        status_code = forum_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_post_id_not_found(self):
        """Test get forum post by id route, with no data"""
        post_id = 1
        response = self.client.get(f"/forum/id/{post_id}")
        status_code = response.status_code

        self.assertEqual(status_code, 404)

    def test_create_post_successful(self):
        """Test creating a post, login required for @jwt_required route"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = create_post_response.status_code

        self.assertEqual(status_code, 201)

    def test_get_post_id_successful(self):
        """Test retrieving a forum post by id after creation"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        post_id = 1
        response = self.client.get(f"/forum/id/{post_id}")
        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_create_post_fail_no_access_token(self):
        """Test creating a forum post without access token"""
        create_post_response = self.client.post("/forum/all", json=example_post)

        status_code = create_post_response.status_code
        expected = {'error': 'authorisation_token', 'message': 'Request does not contain a valid token'}
        result = create_post_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_create_post_fail_invalid_token(self):
        """Test creating a forum post, invalid access token"""
        invalid_token = "invalidtoken"

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {invalid_token}"
            }
        )

        status_code = create_post_response.status_code
        expected = {'error': 'invalid_token', 'message': 'Signature verification failed'}
        result = create_post_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_edit_post_successful(self):
        """Test editing a forum post, login and verified same user required"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        post_id = 1
        original_get_by_id = self.client.get(f"/forum/id/{post_id}")

        update_response = self.client.put(f"/forum/id/{post_id}",
            json=create_post_json(post_content="Changing the content"),
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        after_get_by_id = self.client.get(f"/forum/id/{post_id}")
        original_post = original_get_by_id.json
        changed_post = after_get_by_id.json

        self.assertEqual(status_code, 200)
        self.assertNotEqual(original_post, changed_post)

    def test_edit_post_no_post(self):
        """Test editing a post that does not exist"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        post_id = 1

        update_response = self.client.put(f"/forum/id/{post_id}",
            json=create_post_json(post_content="Changing the content"),
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        result = update_response.json
        expected = {'message': f'Message not found. You have requested this URI [/forum/id/{post_id}] but did you mean'
                               f' /forum/id/<int:id> or /forum/all or /forum/author/<string:author> ?'}

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_edit_post_fail_wrong_user(self):
        """Test editing a post by a different user, unsuccessful"""
        first_register = self.client.post("/user/register", json=default_user)

        first_access_token = first_register.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {first_access_token}"
            }
        )

        post_id = 1
        original_get_by_id = self.client.get(f"/forum/id/{post_id}")

        second_register = self.client.post("/user/register",
            json=create_user_json(username="differentuser", email="differentuser@test.com")
        )

        second_access_token = second_register.json["access_token"]

        update_response = self.client.put(f"/forum/id/{post_id}",
            json=create_post_json(post_content="Changing the content", post_author="differentuser"),
            headers={
                "Authorization": f"Bearer {second_access_token}"
            }
        )

        status_code = update_response.status_code
        after_get_by_id = self.client.get(f"/forum/id/{post_id}")

        original_post = create_post_response.json
        changed_post = after_get_by_id.json
        result = update_response.json
        expected = {'message': 'Unauthorised: You are not the author of this message'}

        self.assertEqual(status_code, 403)
        self.assertEqual(original_post, changed_post)
        self.assertEqual(expected, result)

    def test_delete_post_successful(self):
        """Test deleting a post, login and verified same user required"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        post_id = 1
        original_get_by_id = self.client.get(f"/forum/id/{post_id}")

        delete_response = self.client.delete(f"/forum/id/{post_id}", headers={
                "Authorization": f"Bearer {access_token}"
            })

        status_code = delete_response.status_code
        before_delete_status_code = original_get_by_id.status_code
        after_get_by_id = self.client.get(f"/forum/id/{post_id}")
        after_delete_status_code = after_get_by_id.status_code

        self.assertEqual(status_code, 200)
        self.assertEqual(after_delete_status_code, 404)
        self.assertNotEqual(before_delete_status_code, after_delete_status_code)

    def test_delete_post_fail_wrong_user(self):
        """Test deleting a post by a different user, unsuccessful"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        post_id = 1
        original_get_by_id = self.client.get(f"/forum/id/{post_id}")

        second_register = self.client.post("/user/register",
            json=create_user_json(username="differentuser", email="differentuser@test.com")
        )

        second_access_token = second_register.json["access_token"]

        delete_response = self.client.delete(f"/forum/id/{post_id}", headers={
                "Authorization": f"Bearer {second_access_token}"
            })

        status_code = delete_response.status_code
        result = delete_response.json
        expected = {'message': 'Unauthorised: You are not the author of this message'}
        before_delete_status_code = original_get_by_id.status_code
        after_get_by_id = self.client.get(f"/forum/id/{post_id}")
        after_delete_status_code = after_get_by_id.status_code

        self.assertEqual(status_code, 403)
        self.assertEqual(expected, result)
        self.assertEqual(before_delete_status_code, after_delete_status_code)

    def test_delete_post_no_post(self):
        """Test deleting a post that does not exist"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        post_id = 1

        delete_response = self.client.delete(f"/forum/id/{post_id}", headers={
                "Authorization": f"Bearer {access_token}"
            })
        
        status_code = delete_response.status_code
        result = delete_response.json
        expected = {'message': f'Message not found. You have requested this URI [/forum/id/{post_id}] but did you mean'
                               f' /forum/id/<int:id> or /forum/all or /forum/author/<string:author> ?'}

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_delete_post_fail_no_token(self):
        """Test deleting a post without an access token"""
        register_response = self.client.post("/user/register", json=default_user)

        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        post_id = 1

        delete_response = self.client.delete(f"/forum/id/{post_id}")

        status_code = delete_response.status_code
        expected = {'error': 'authorisation_token', 'message': 'Request does not contain a valid token'}
        result = delete_response.json

        self.assertEqual(expected, result)
        self.assertEqual(status_code, 401)

    def test_get_post_by_category_results(self):
        """Test get a list of forum posts by category with results"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        category = "Test"
        get_response = self.client.get(f"/forum/category/{category}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_post_by_category_no_results(self):
        """Test get list of forum posts in a category, no matches"""
        category = "Test"
        get_response = self.client.get(f"/forum/category/{category}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)
    
    def test_get_post_by_author_results(self):
        """Test get a list of forum posts by a specific username with results"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        author = "testuser"
        get_response = self.client.get(f"/forum/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_post_by_author_no_results(self):
        """Test get list of forum posts by a specific username, no matches"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        create_post_response = self.client.post("/forum/all",
            json=example_post,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        author = "differentuser"
        get_response = self.client.get(f"/forum/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)


if __name__ == "__main__":
    unittest.main()
