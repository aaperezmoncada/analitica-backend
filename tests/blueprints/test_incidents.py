import unittest
from flask import Flask

from src.blueprints.services import get_incidents
from src.main import create_app, logger


class TestIncidentEndpoints(unittest.TestCase):
    @classmethod
    def test_incidents(self):
        company = 'uniandes'
        response = get_incidents('/incidents/get_incidents/{company}')
        #self.assertEqual(response, 200)
        #self.assertIsInstance(response.get_json(), list)

    def test_search_incident(self):
        payload = {
            "userId": 1,
            "incidentId": 1,
            "company": 'uniandes'
        }
        #response =  self.client.post('/incidents/search_incident', json=payload)
        #self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()