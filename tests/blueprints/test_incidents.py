import unittest
from unittest.mock import patch, Mock
from src.clients.manage_incident import IncidentClient
from src.commands.get_incidents import GetIncidents

class TestIncidentEndpoints(unittest.TestCase):
    @patch.object(IncidentClient, "get_incidents")

    def test_execute_success(self, mock_get_incidents):
        mock_get_incidents.return_value = Mock(json=Mock(return_value=[
            {
                'agentId': 1,
                'type': 'QUEJA',
                'date': '2024-01-01',
                'channel': 'WEB',
                'solved': True,
                'userId': 2
            }
        ]))

        params = {
            'agenteId': '1',
            'tipoIncidente': 'QUEJA',
            'fechaInicio': '2024-01-01',
            'fechaFin': '2024-01-02'
        }

        command = GetIncidents('uniandes', params)
        result = command.execute()

        assert result['total_incidentes'] == 1
        assert result['incidentes_resueltos'] == 1
        assert result['global_recommendation'] == 'El proceso está funcionando correctamente, se debe seguir con el enfoque actual.'

    @patch('src.commands.get_incidents.GetIncidents.registro_filtrado')
    @patch('src.commands.get_incidents.IncidentClient.get_incidents')
    def test_execute_with_filter(self, mock_get_incidents, mock_registro_filtrado):
        mock_get_incidents.return_value = Mock(json=Mock(return_value=[
            {
                'agentId': 1,
                'type': 'QUEJA',
                'date': '2024-01-01',
                'channel': 'WEB',
                'solved': True,
                'userId': 1
            }
        ]))

        # Filtro para el caso
        mock_registro_filtrado.return_value = True

        params = {
            'agenteId': '1',
            'tipoIncidente': 'QUEJA',
            'fechaInicio': '2024-01-01',
            'fechaFin': '2024-01-02'
        }

        command = GetIncidents('uniandes', params)
        result = command.execute()

        # Verificar que los filtros se aplican correctamente
        mock_registro_filtrado.assert_called_once()
        assert result['total_incidentes'] == 1
        assert result['incidentes_resueltos'] == 1


if __name__ == '__main__':
    unittest.main()