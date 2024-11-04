import requests
import os

class IncidentClient:
    def __init__(self):
        self.incident_path = "http://incidents-microservice:5003"
        if os.environ.get("INCIDENT_PATH"):
            self.incident_path = os.environ.get("INCIDENT_PATH")
        self.headers = {"Content-Type": "application/json"}

    def get_incidents(self, company):
        get_data_incidents_url = f'{self.incident_path}/incidents/get_incidents/{company}'
        return requests.get(get_data_incidents_url)

    def get_user_id(self, user_id, company):
        get_data_user_url = f'{self.incident_path}/incidents/get_user/{user_id}/{company}'
        return requests.get(get_data_user_url)
