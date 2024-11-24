import unittest
from unittest.mock import patch, MagicMock
from src.errors.errors import BadRequest, PreconditionFailed

class TestCreateUserCommand(unittest.TestCase):
    def setUp(self):
        self.valid_json = {
            'id': '1',
            'name': 'John Doe',
            'phone': '1234567890',
            'email': 'john.doe@example.com',
            'company': 'Example Inc.'
        }


if __name__ == '__main__':
    unittest.main()