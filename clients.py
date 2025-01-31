import pandas as pd

clients_df = pd.read_csv('clients.csv')
plants_df = pd.read_csv('plants.csv')

class Client:
    def __init__(self, clients_df, client_id:int):
        self._client_id = client_id
        self._coord = (clients_df['coord_x'][client_id], clients_df['coord_y'][client_id])
        self._capacity = clients_df['capacity'][client_id]
        self._init = clients_df['init'][client_id]
        self._consumption = clients_df['consumption'][client_id]
        
class Clients:
    def __init__(self, clients_df):
        self._clients = {}
        for i in range(len(clients_df)):
            self._clients[i] = Client(clients_df, i)
            
    def get_client(self, client_id:int):
        return self._clients[client_id]
    
    def get_clients(self):
        return self._clients