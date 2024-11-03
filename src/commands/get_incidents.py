import datetime

from src.clients.manage_client import ManageClient
from src.commands.base_command import BaseCommand


class GetIncidents(BaseCommand):
    def __init__(self, json):
        self.agenteId = json.get('agenteId', None)
        self.tipoIncidente = json.get('tipoIncidente', None)
        self.fecha_inicio = json.get('fechaInicio', None)
        self.fecha_fin = json.get('fechaFin', None)
        self.incidents = json.get('data', None)
        self.channels = json.get('count_channels', None)

    def execute(self):
        try:
            manageClient = ManageClient()
            sin_solucion = [0] * 7
            con_solucion = [0] * 7
            incidents_canal = [0] * self.channels
            contador_agentes = {}
            max_agentes = 2
            incidentes_resueltos = 0

            for value in self.incidents:
                if value.resuelto:
                    # Totalizador de incidentes por semana resueltos
                    con_solucion[value.date.weekday()] += 1

                    # Totalizador de incidentes resueltos
                    incidentes_resueltos += 1
                else:
                    # Totalizador de incidentes por semana sin resolver
                    sin_solucion[value.date.weekday()] += 1

                    # Agrupamiento de incidentes sin resolver por agente
                    if not value.user_id in contador_agentes:
                        cliente = manageClient.get_data_user(value.user_id)
                        contador_agentes[value.user_id] = {'name': cliente.name if cliente else 'NN', 'count': 1}
                    else:
                        contador_agentes[value.user_id]['count'] += 1

                # Totalizador de incidentes por canal
                index_canal = value.channel.value-1
                incidents_canal[index_canal] += 1

            # Ordenamiento de agentes de mayor a menor según los casos sin resolver.
            lista_agentes = list(map(lambda item: item['name'], sorted(contador_agentes.values(), key=lambda x: x['count'], reverse=True)))

            incidents_info = {
                'total_incidentes': len(self.incidents),
                'total_usuarios': len(contador_agentes),
                'incidentes_resueltos': incidentes_resueltos,
                'incidentes_canal': incidents_canal,
                'sin_solucion': sin_solucion,
                'con_solucion': con_solucion,
                'lista_agentes': lista_agentes[:max_agentes],
            }

            return incidents_info

        except Exception as e:
            raise e