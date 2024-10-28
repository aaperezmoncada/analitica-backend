import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from src.main import create_app
from src.models.incident import db, Incident
from src.blueprints.services import clear_database
import json

class TestClearDatabaseEndpoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing', local=True)
        cls.incident = cls.app.test_incident()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_clear_database_success(self):
        response = self.incident.post('/analitica/clear_database')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Database cleared successfully'})


if __name__ == '__main__':
    unittest.main()