import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig


def create_user_json(username="testuser", first_name="test", last_name="user", email="testuser@test.com",
                     password="mytestpassword"):
    """Function to create user registration json"""
    json = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password
            }
    return json


default_user = create_user_json()

expired_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDAxNzcwMiwianRpI" \
                "joiMWQ0NTRmNTEtNTU5MS00Y2MzLWJkODMtMmM5M2U1MDlkMTc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRl" \
                "c3R1c2VyIiwibmJmIjoxNzEwMDE3NzAyLCJjc3JmIjoiODk5NzAzM2MtZTQwNi00OWNiLTlkMmMtYzVlYTM5NmQw" \
                "ZTczIiwiZXhwIjoxNzEwMDE4NjAyfQ.oYms99qrpe01vZRD9bZu8ChuE2HR-7eN9w99hlKvCqc"


class TestAPI(TestCase):
    """Base test class for setting up test database and tables"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():

            db.create_all()
    
    def tearDown(self):
        """Destroy all the instances created for testing, remove sessions and drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
