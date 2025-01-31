import pandas as pd

plants_df = pd.read_csv('plants.csv')

class Plants:
    """Class that regroup the factories."""

    def __init__(self, factories: list["Plant"]):
        self._plants=factories

class Plant:
    """Class that define a factorie."""

    def __init__(self, coord:tuple, capacity:int, init:int, refill:int, plants_id:int):
        self._coord=coord
        self._capacity=capacity
        self._init=init
        self._refill=refill
        self._plants_id=plants_id

def create_plants(plants_df):
    L=[]
    for i in range (len(plants_df)):
        plant=Plant((plants_df['coord_x'][i],plants_df['coord_y'][i]),plants_df['capacity'][i],plants_df['init'][i],plants_df['refill'][i],i)
        L.append(plant)
    plants=Plants(L)
    return plants
    
plants=create_plants(plants_df)
