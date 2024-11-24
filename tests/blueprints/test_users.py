import unittest
from unittest.mock import patch, Mock

from flask import Flask

from src.commands.get_user import GetUser
from src.errors.errors import NotFound
from src.main import create_app, logger

class TestUserEndpoints(unittest.TestCase):
    @classmethod
    @patch('src.commands.get_user.User')
    def test_get_user_success(self, mock_user):
        # Aquí puedes simular el comportamiento esperado de la clase User
        mock_user.return_value = Mock(id=1, name="John Doe")
        response = mock_user.get_user()
        assert response.name == "John Doe"

    # @patch("src.commands.get_user.GetUser.execute")
    # def test_execute_success(self, mock_execute):
    #     # Mock de la respuesta para un usuario encontrado
    #     mock_execute.return_value = {
    #         'id': 1,
    #         'name': 'John Doe',
    #         'phone': '1234567890',
    #         'email': 'john@example.com',
    #         'incidents': []
    #     }
    #
    #     command = GetUser(1)
    #     result = command.execute()
    #
    #     # Verificar el resultado
    #     assert result['id'] == 1
    #     assert result['name'] == 'John Doe'
    #     assert result['phone'] == '1234567890'
    #
    # @patch("src.commands.get_user.GetUser.execute")
    # def test_execute_user_not_found(self, mock_execute):
    #     # Simular el error de 'Usuario no encontrado'
    #     mock_execute.side_effect = NotFound("User not found")
    #
    #     command = GetUser(999)
    #
    #     with self.assertRaises(NotFound):
    #         command.execute()

if __name__ == '__main__':
    unittest.main()