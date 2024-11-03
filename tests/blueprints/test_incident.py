import unittest
import json
from flask import Flask
from src.main import create_app

class TestIncidentEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing', local=True)
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_incidents(self):
        response = self.client.get('/analitica/get_incidents')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Incident with id nonexistent_id not found', response.get_json()['error'])

    def test_get_incident_not_found(self):
        response = self.incident.get('/analitica/get_incident/nonexistent_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Incident with id nonexistent_id not found', response.get_json()['error'])

    def test_ping(self):
        response = self.incident.get('/incident/ping')
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()