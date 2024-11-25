import unittest
from flask import Flask
from src.main import create_app

class TestPingEndpoint(unittest.TestCase):
    pass
    # def setUp(self):
    #     self.app = create_app('testing', local=True)
    #     self.client = self.app.test_client()
    #     #self.incident = self.app.test_incidents()
    #
    # def test_ping(self):
    #     response = self.client.get('/incidents/ping')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json, {'message': 'pong'})

if __name__ == '__main__':
    unittest.main()