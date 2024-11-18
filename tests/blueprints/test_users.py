import unittest
from flask import Flask
from src.main import create_app, logger

class TestUserEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing', local=True)
        cls.client = cls.app.test_client()

    def create_user(self):
        user_payload = {
            "id": "12345",
            "name": "Test User",
            "phone": "1234567890",
            "email": "testuser@example.com",
            "company": "uniandes"
        }
        user_response = self.client.post('/incidents/create_user', json=user_payload)
        self.user_id = user_response.get_json(user_payload['id'])
        logger.info(f"Created user: {user_response.get_json()}")
        return user_response, user_payload["company"]

    def test_get_user(self):
        user_response= ''
        company = 'uniandes'
        user_id = 1
        response = self.client.get(f'/incidents/get_user/{user_id}/{company}')
        #self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), dict)
        self.assertEqual(1, user_id)

if __name__ == '__main__':
    unittest.main()