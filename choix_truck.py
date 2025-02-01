
import places as pl
import pandas as pd 
import numpy as np
import math as m
import utils as u

clients_df = pd.read_csv('clients.csv')
plants_df = pd.read_csv('plants.csv')

def choose_trucks(truck, places):
    truck_co = truck.coord
    if truck.filled_bottles==0:
        plants = [place for place in places if place._type=="plant"]
        for plant in plants:
            if plant != truck.destination:
                coord2=plant._coord
                cost = -0.1*u.distance(truck_co,coord2)
                costs.append(cost)
        i_min=np.argmin(costs)
        id=plants[i_min].id
    else : 
        clients = [place for place in places if place._type=="client"]
        costs = []
        for client in clients:
            if client != truck.destination:
                coord2=client._coord
                unavailable = u.count(client._stock, None)
                available = int(client._capacity-unavailable)
                cost=-u.distance(truck_co,coord2)*0.1+max(truck.filled_bottles,available)*60
                costs.append(cost)
        i_min=np.argmin(costs)
        id=clients[i_min]._place_id
        cost = min(costs)
    return id, cost


