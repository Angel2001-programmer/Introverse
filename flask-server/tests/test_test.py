import unittest
from test_api import TestForumAPI

class Test(TestForumAPI):
    def test_get_all_posts(self):
        """Test getting all forum posts"""
        forum_response = self.client.get("/forum/all")

        status_code = forum_response.status_code

        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()