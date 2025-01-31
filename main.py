import places as pl
import pandas as pd 
import numpy as np

clients_df = pd.read_csv('clients.csv')
plants_df = pd.read_csv('plants.csv')

def initialisation_places(clients_df, plants_df):
    """Initialisation of the places."""
    places = []
    for i in range(len(plants_df)):
        place = pl.Place(coord=(plants_df.loc[i, 'coord_x'], plants_df.loc[i, 'coord_y']),
                         capacity=plants_df.loc[i, 'capacity'],
                         init=plants_df.loc[i, 'init'],
                         flow=plants_df.loc[i, 'refill'],
                         place_id=i,
                         type='plant')
        places.append(place)
    for i in range(len(clients_df)):
        place = pl.Place(coord=(clients_df.loc[i, 'coord_x'], clients_df.loc[i, 'coord_y']),
                         capacity=clients_df.loc[i, 'capacity'],
                         init=clients_df.loc[i, 'init'],
                         flow=clients_df.loc[i, 'consumption'],
                         place_id=i,
                         type='client')
        places.append(place)
    return places




class Places:
    def __init__(self):
        L_plants = []
        for i in range(len(plants_df)):
            plant = pl.Place(coord=(plants_df.loc[i, 'coord_x'], plants_df.loc[i, 'coord_y']),
                         capacity=plants_df.loc[i, 'capacity'],
                         init=plants_df.loc[i, 'init'],
                         flow=plants_df.loc[i, 'refill'],
                         place_id=i,
                         type='plant')
            L_plants.append(plant)
            self.plants=L_plants
        L_clients=[]
        for i in range(len(clients_df)):
            client = pl.Place(coord=(clients_df.loc[i, 'coord_x'], clients_df.loc[i, 'coord_y']),
                         capacity=clients_df.loc[i, 'capacity'],
                         init=clients_df.loc[i, 'init'],
                         flow=clients_df.loc[i, 'consumption'],
                         place_id=i,
                         type='client')
            L_clients.append(client)
        self.clients=client
        




places = initialisation_places(clients_df, plants_df)

def afficher_places(places):
    """Display the places."""
    for place in places:
        print(f"Place ID: {place._place_id}, Type: {place._type}, Coord: {place._coord}, Capacity: {place._capacity}, Stock: {place._stock}, Flow: {place._flow}")
    
afficher_places(places)