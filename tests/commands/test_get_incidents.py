import unittest
from datetime import datetime

from flask import Flask, request, jsonify

import src.clients.manage_client
from src.blueprints.services import get_incidents
from src.commands.get_incidents import GetIncidents, FORMAT_DATE
from src.main import create_app

class TestPingEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing', local=True)
        self.client = self.app.test_client()

    def test_ping(self):
        response = self.client.get('/incidents/ping')
        # self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json, {'message': 'pong'})

class TestGetIncidents(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing', local=True)
        self.incidents = {
                'id':'a6cc932a-6614-4346-b1db-f78b79480a95',
                'type':'QUEJA',
                'channel':'MOBILE',
                'description':'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.',
                'date':'2024-01-11',
                'user_id':1,
                'agent_id':1,
                'solved': True,
                'company': 'uniandes',
                'response':''
            }
        resultado = get_incidents('uniandes')
        return jsonify('resultado'), 200

class TestIncidentClient(unittest.TestCase):
    def test_get_incidents(self, company):
        self.company = 'uniandes'
        incidentes = get_incidents('uniandes', company)

    def test_user_id(self,user_id, company ):
        self.user_id = user_id
        self.company = company
        user = src.clients.manage_client.ManageClient.get_data_user(user_id, self.company)


if __name__ == '__main__':
    unittest.main()