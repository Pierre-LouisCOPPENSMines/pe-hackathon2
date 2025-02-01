class Place:
    """Class that define a place."""

    def __init__(self, coord:tuple, capacity:int, init:int, flow:float, place_id:int, type:str):
        self._coord=coord
        self._capacity=capacity
        self._type = type
        if (self._type == "plant"):
            self._flow=flow
            self._stock= [True for i in range(init)] + [None for i in range(capacity-init)]
        elif (self._type == "client"):
            self._flow=-flow
            self._stock= [False for i in range(init)] + [None for i in range(capacity-init)]
        else: 
            raise ValueError("The type of the place must be either plant or client.")
        self._place_id=place_id 
        

class Places:
    def __init__(self,clients_df, plants_df):
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
        
        
        

