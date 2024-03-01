import unittest
from test_api import TestAPI, create_user_json, default_user


class TestContentAPI(TestAPI):
    """Tests for content namespace routes"""

    def test_hello_world(self):
        """Test the hello world route"""
        hello_response = self.client.get("/content/hello")
        result = hello_response.json
        expected = {"message": "Hello world!"}

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()