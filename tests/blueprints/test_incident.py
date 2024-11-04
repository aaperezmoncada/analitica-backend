import unittest
from src.main import create_app

class TestIncidentEndpoints(unittest.TestCase):

    @classmethod
    def test_get_incidents(self):
        pass
    #     response = self.incidents.get('/analitica/get_incidents')
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn('Incident with id nonexistent_id not found', response.get_json()['error'])



if __name__ == '__main__':
    unittest.main()