import unittest
from test_auth_api import TestAPI, create_user_json, default_user, expired_token
from routes.user import check_email
from flask_jwt_extended import create_access_token


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

        status_code = get_response.status_code
        self.assertEqual(status_code, 200)

    def test_get_profile_fail_no_user(self):
        """Test get profile if user does not exist, using a token"""
        with self.app.app_context():
            access_token = create_access_token(identity="Tester")

        get_response = self.client.get(f"/user/current_user",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = get_response.status_code
        expected = {'message': 'Unauthorised'}
        result = get_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)
    
    def test_get_profile_fail_no_token(self):
        """Test get profile without a token"""
        register_response = self.client.post("/user/register", json=default_user)

        get_response = self.client.get(f"/user/current_user")

        status_code = get_response.status_code
        expected = {'error': 'authorisation_token', 'message': 'Request does not contain a valid token'}
        result = get_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_edit_profile_interests_successful(self):
        """Test edit interests in profile successfully"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "interests": "I like testing"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'first_name': 'test', 'last_name': 'user', 'email': 'testuser@test.com', 'date_of_birth': None,
                    'interests': 'I like testing'}
        result = update_response.json

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_edit_profile_date_of_birth_successful(self):
        """Test edit date of birth in profile successfully"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "date_of_birth": "1999-12-01"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'first_name': 'test', 'last_name': 'user', 'email': 'testuser@test.com',
                    'date_of_birth': 'Wed, 01 Dec 1999 00:00:00 -0000', 'interests': None}
        result = update_response.json

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_edit_profile_date_of_birth_fail_format(self):
        """Test edit date of birth in profile, wrong date format"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "date_of_birth": "1999.12.01"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'message': 'Invalid date format'}
        result = update_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_edit_profile_date_of_birth_invalid_month(self):
        """Test edit date of birth in profile, invalid month"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "date_of_birth": "1999-20-01"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'message': 'Invalid date format'}
        result = update_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_edit_profile_date_of_birth_invalid_date(self):
        """Test edit date of birth in profile, invalid date"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "date_of_birth": "1999-04-31"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'message': 'Invalid date format'}
        result = update_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_edit_profile_interests_fail_no_user(self):
        """Test edit interests in profile if user does not exist, using a token"""
        with self.app.app_context():
            access_token = create_access_token(identity="Tester")

        update_response = self.client.put(f"/user/current_user",
            json={
                "interests": "I like testing"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code

        self.assertEqual(status_code, 401)
        expected = {'message': 'Unauthorised'}
        result = update_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_edit_profile_fail_unsupported_field(self):
        """Test trying to edit something else in profile"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "username": "newusername"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'message': 'Nothing to update'}
        result = update_response.json

        self.assertEqual(status_code, 400)
        self.assertEqual(expected, result)

    def test_edit_profile_partial_fail_two_things_same_time(self):
        """Test trying to edit both valid fields in same payload, only first executed (restrict to one in frontend)"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        update_response = self.client.put(f"/user/current_user",
            json={
                "interests": "I like testing",
                "date_of_birth": "1999-12-01"
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = update_response.status_code
        expected = {'first_name': 'test', 'last_name': 'user', 'email': 'testuser@test.com', 'date_of_birth': None,
                    'interests': 'I like testing'}
        result = update_response.json

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_refresh_token_successful(self):
        """Come back to these later"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        refresh_response = self.client.post(f"/user/refresh",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        result = refresh_response.json
        status_code = refresh_response.status_code

        self.assertEqual(status_code, 200)
        self.assertTrue(result["access_token"])
        
    def test_refresh_token_fail_expired_token(self):
        """Come back to these later"""
        register_response = self.client.post("/user/register", json=default_user)
        access_token = register_response.json["access_token"]

        refresh_response = self.client.post(f"/user/refresh",
            headers={
                "Authorization": f"Bearer {expired_token}"
            }
        )

        status_code = refresh_response.status_code
        expected = {'error': 'token_expired', 'message': 'Token has expired'}
        result = refresh_response.json

        self.assertEqual(status_code, 401)
        self.assertEqual(expected, result)

    def test_logout_successful(self):
        """Test logging out successfully"""
        register_response = self.client.post("/user/register", json=default_user)
        logout_response = self.client.post(f"/user/logout")

        status_code = logout_response.status_code
        expected = {'message': 'Logout successful'}
        result = logout_response.json

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_members_results_in_list(self):
        """Test getting list of all users successfully, may move this to admin space in future"""
        register_response = self.client.post("/user/register", json=default_user)
        member_response = self.client.get(f"/user/members")
        status_code = member_response.status_code
        result = member_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_all_members_no_users(self):
        """Test getting list of all users, empty list"""
        get_response = self.client.get(f"/user/members")
        status_code = get_response.status_code
        expected = []
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)
        self.assertEqual(expected, result)
    
    def test_search_member_successfully(self):
        """Test searching a user by username, may move this to admin space in future"""
        register_response = self.client.post("/user/register", json=default_user)
        member = "testuser"
        member_response = self.client.get(f"/user/members/{member}")

        status_code = member_response.status_code
        result = member_response.json["first_name"]
        expected = "test"

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_search_member_not_found(self):
        """Test searching a user by username, no user exists"""
        member = "testuser"
        member_response = self.client.get(f"/user/members/{member}")
        
        status_code = member_response.status_code
        expected = {'message': f'User not found. You have requested this URI [/user/members/{member}] but did you mean '
                               f'/user/members/<string:member> or /user/members or /user/register ?'}
        result = member_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
