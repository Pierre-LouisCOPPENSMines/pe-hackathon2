from main import Places
import places as pl
import pandas as pd 
import numpy as np

clients_df = pd.read_csv('clients.csv')
plants_df = pd.read_csv('plants.csv')

places=Places(clients_df, plants_df)

def distance(x,y):
    d=(x[0]-y[0])**2+(x[1]-y[1])**2


def choix_trucks(L_trucks:list):

    for truck in L_trucks:
        coord1=truck.coord

        if truck.filled_bottles==0:
            L_plants=places.plants
            L_dist=[]
            for plant in L_plants:
                coord2=plant.coord
                d=distance(coord1,coord2)
                L_dist.append(d)
        i_min=np.argmin(L_dist)
        distance=min(L_dist)
        id_plant=L_plants[i_min].id
        #appel fonction Noémie et Pierre-Louis
        cost=-0.1*distance

    else:
        if truck.filled_bottles==0:
            L_clients=places.clients
            L_cost=[]
            for client in L_clients:
                coord2=client.coord
                cost=-distance(coord1,coord2)*0.1+np.max(truck.filled_bottles,int(client._capacity-client._stock))*60
                L_dist.append(cost)
        i_min=np.argmin(L_cost)
        distance=min(L_cost)
        id_client=L_clients[i_min].id
    #appel fonction Noémie et Pierre-Louis




