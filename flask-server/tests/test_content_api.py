import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig

class TestContentAPI(TestCase):
    """Tests for content namespace routes"""

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

        self.assertEqual(expected, result)

    def tearDown(self):
        """Destroy all the instances created for testing, remove sessions and drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()