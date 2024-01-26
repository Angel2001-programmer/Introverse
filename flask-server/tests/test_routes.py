import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig
from routes import register_user

# Still problems with initialisation

class APITestCase(TestCase):
    # This function will set up our test database
    def setUp(self):
        self.app=create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)

            db.create_all()


    def test_home_response(self):
        home_response = self.client.get('/')
        result = home_response.json
        expected = {"message":"hello"}

        self.assertEqual(expected, result)

    
    def test_register_user_success(self):
        pass


    # This function will remove everything from our test database
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()