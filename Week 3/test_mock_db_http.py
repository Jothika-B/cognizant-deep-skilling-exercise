import unittest
from unittest.mock import patch


# Function that simulates DB call
def get_user_from_db():
    return "Real User"


# Function that simulates HTTP request
def fetch_api_data():
    return {"status": "real"}


class TestMocking(unittest.TestCase):

    @patch('__main__.get_user_from_db')
    def test_mock_db_call(self, mock_db):
        mock_db.return_value = "Mock User"

        result = get_user_from_db()

        self.assertEqual(result, "Mock User")

    @patch('__main__.fetch_api_data')
    def test_mock_http_request(self, mock_http):
        mock_http.return_value = {"status": "success"}

        result = fetch_api_data()

        self.assertEqual(result["status"], "success")


if __name__ == "__main__":
    unittest.main()
