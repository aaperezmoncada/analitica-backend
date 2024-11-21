import datetime
import json
import sys
import traceback

from flask import jsonify

from src.clients.manage_client import ManageClient
from src.clients.manage_incident import IncidentClient
from src.commands.base_command import BaseCommand

FORMAT_DATE = '%a, %d %b %Y %H:%M:%S %Z'

class GetIncidents(BaseCommand):
    def __init__(self, company, json):
        self.company = company
        self.agenteId = json.get('agenteId', None)
        self.tipoIncidente = json.get('tipoIncidente', None)
        self.fecha_inicio = json.get('fechaInicio', None)
        self.fecha_fin = json.get('fechaFin', None)
        if self.fecha_inicio:
            self.fecha_inicio = self.get_date(self.fecha_inicio)
        if self.fecha_fin:
            self.fecha_fin = self.get_date(self.fecha_fin)

    def get_weekday(self, date_str):
        try:
            return self.get_date(date_str, FORMAT_DATE).weekday()
        except:
            return -1 # No encontrado

    def get_date(self, date_str, format='%Y-%m-%d'):
        try:
            return datetime.datetime.strptime(date_str, format).date()
        except:
            return None # No encontrado

    def registro_filtrado(self, value):
        if self.agenteId and self.agenteId!='' and self.agenteId!=value['agentId']:
            return False
        if self.tipoIncidente and self.tipoIncidente!='' and self.tipoIncidente!=value['type']:
            return False
        fecha_value = self.get_date(value['date'], FORMAT_DATE)
        if self.fecha_inicio and fecha_value < self.fecha_inicio:
            return False
        if self.fecha_fin and fecha_value > self.fecha_fin:
            return False
        return True

    def execute(self):
        try:
            incidentClient = IncidentClient()
            manageClient = ManageClient()
            incidents = incidentClient.get_incidents(self.company).json()

            sin_solucion = [0] * 7
            con_solucion = [0] * 7
            incidents_canal = [0] * 2 #Actualizar según Enum de Channel
            contador_agentes = {}
            listado_agentes = {}
            contador_usuarios = {}
            lista_agentes_id = []
            max_agentes = 2
            incidentes_resueltos = 0
            incidentes_sin_resolver = 0
            global_recommendation = ''
            total = 0

            for value in incidents:
                if not value['agentId'] in listado_agentes.keys():
                    try:
                        user = manageClient.get_data_user(value['agentId']).json()
                        lista_agentes_id.append({
                            'id': value['agentId'],
                            'name': user['name'],
                        })
                    except:
                        user = None
                    listado_agentes[value['agentId']] = user

                if not self.registro_filtrado(value):
                    continue

                weekday = self.get_weekday(value['date'])
                if value['solved']:
                    # Totalizador de incidentes por semana resueltos
                    if weekday != -1:
                        con_solucion[weekday] += 1

                    # Totalizador de incidentes resueltos
                    incidentes_resueltos += 1
                else:
                    incidentes_sin_resolver += 1
                    # Totalizador de incidentes por semana sin resolver
                    if weekday != -1:
                        sin_solucion[weekday] += 1

                    # Agrupamiento de incidentes sin resolver por agente
                    if not value['agentId'] in contador_agentes:
                        agente = listado_agentes[value['agentId']]
                        contador_agentes[value['agentId']] = {'name': agente['name'] if agente else 'NN', 'id': value['agentId'], 'count': 1}
                    else:
                        contador_agentes[value['agentId']]['count'] += 1
                contador_usuarios[value['userId']] = True
                # Totalizador de incidentes por canal
                if value['channel'] == 'WEB':
                    incidents_canal[0] += 1
                elif value['channel'] == 'MOBILE':
                    incidents_canal[1] += 1
                elif value['channel'] == 'TELEFONO':
                    incidents_canal[1] += 1
                elif value['channel'] == 'CORREO':
                    incidents_canal[1] += 1
                total += 1

            lista_agentes = list(map(lambda item: item['name'], sorted(contador_agentes.values(), key=lambda x: x['count'], reverse=True)))
            if incidents:
                if incidentes_resueltos > incidentes_sin_resolver:
                    if incidentes_sin_resolver > 0:
                        global_recommendation = "Evaluar el desempeño de los agentes y asignar recursos de manera más eficiente."
                    else:
                        global_recommendation = "El proceso está funcionando correctamente, se debe seguir con el enfoque actual."
                elif incidentes_sin_resolver > incidentes_resueltos:
                    global_recommendation = "Es necesario escalar más incidentes o mejorar la asignación de recursos."
                else:
                    global_recommendation = "Evaluar el desempeño de los agentes y asignar recursos de manera más eficiente."
            else:
                global_recommendation = "Se puede determinar el correcto funcionamiento del servicio, sin embargo se recomienda aplicar otras alternativas de verificación como encuestas de satisfacción "
            incidents_info = {
                'total_incidentes': total,
                'total_usuarios': len(contador_usuarios),
                'incidentes_resueltos': incidentes_resueltos,
                'incidentes_canal': incidents_canal,
                'sin_solucion': sin_solucion,
                'con_solucion': con_solucion,
                'agentes': lista_agentes_id,
                'lista_agentes': lista_agentes[:max_agentes],
                'global_recommendation': global_recommendation
            }

            return incidents_info

        except Exception as e:
            raise e