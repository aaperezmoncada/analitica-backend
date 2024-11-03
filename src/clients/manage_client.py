import requests
import os

class ManageClient:
    def __init__(self):
        self.client_path = "http://clientes-microservice:5001"
        if os.environ.get("CLIENT_PATH"):
            self.client_path = os.environ.get("CLIENT_PATH")
        self.headers = {"Content-Type": "application/json"}

    def get_data_user(self, id_user):
        get_data_client_url = f'{self.client_path}/clients/get_client/{id_user}'
        return requests.get(get_data_client_url)