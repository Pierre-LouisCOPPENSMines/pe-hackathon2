import places as pl
import pandas as pd 
import truck as tr
import numpy as np
import heapq as hq
import choix_truck as ct
import display as d 
clients_df = pd.read_csv('clients.csv')
plants_df = pd.read_csv('plants.csv')
speed = 50 / 3.6 # Speed in m/s
time_list = [] # List of arrival times


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


places = initialisation_places(clients_df, plants_df)


#places = initialisation_places(clients_df, plants_df)

def afficher_places(places):
    """Display the places."""
    for place in places:
        print(f"Place ID: {place._place_id}, Type: {place._type}, Coord: {place._coord}, Capacity: {place._capacity}, Stock: {place._stock}, Flow: {place._flow}")
    
afficher_places(places)


def initialisation_camions():
    """Initialisation of the trucks."""
    trucks = []
    for i in range(10):
        truck = tr.Truck((0,0),"parked",i,40,40,places[0])
        trucks.append(truck)
    return trucks

trucks = initialisation_camions()

def afficher_camions(trucks):
    """Display the trucks."""
    for truck in trucks:
        print(f"Truck ID: {truck.id}, Coord: {truck.coord}, State: {truck.state}, Empty bottles: {truck.empty_bottles}, Filled bottles: {truck.filled_bottles}")
        
afficher_camions(trucks)

#studied_situation = [(truck, places[0]) for truck in trucks] # List of tuples (Trucks, Places) that we are studying at the specific time 

def generate_random_place():
    """Generate a random place."""
    return np.random.choice(places)


def main():
    """Start the simulation."""
    time = 0  
    while time < 180:
        time = update(time)
        if len(time_list) == 0: 
            break 
    d.draw_itinerary(trucks[0])
    
    
        

def update(t): 
    """Update the time and the state of the trucks"""
    #studied_situation = []
    for truck in trucks : 
        # Track trucks arriving at destination
        if (truck.arrival_time - t) < 0.1:
            truck.state = "parked"
        #Give a new destination to this trucks
        if truck.state == "parked":
            truck.coord = truck.destination._coord  # la destination est encore le lieu où il est garé
            print(ct.choose_trucks(truck, places))
            place_id = ct.choose_trucks(truck, places)[0]
            go_to_place = places[place_id]
            truck.destination = go_to_place
            truck.itinerary.append(go_to_place)
            truck.state = "riding"
            distance_step = np.linalg.norm(np.array(truck.coord) - np.array(truck.destination._coord))
            truck.arrival_time += distance_step / speed
            time_list.append(truck.arrival_time)
            print(f"Truck {truck.id} is riding to {truck.destination._place_id} and departure at {t} will arrive at {truck.arrival_time}")
    time_list.sort(reverse = True)
    t = time_list.pop()
    return t 

main()
            
    
        
    
        