
def draw_itinerary(truck):
    import matplotlib.pyplot as plt

    x_coords = [place._coord[0] for place in truck.itinerary]
    y_coords = [place._coord[1] for place in truck.itinerary]

    plt.plot(x_coords, y_coords, marker='o')
    plt.title('Truck Itinerary')
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.grid(True)
    plt.show()
