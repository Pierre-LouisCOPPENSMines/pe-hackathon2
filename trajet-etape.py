class Trajet:
    def __init__(self, origine, destination, camion, distance=None, temps=None):

        self.origine = origine
        self.destination = destination
        self.camion = camion
        self.distance = distance if distance is not None else self.calculer_distance()
        self.temps = temps if temps is not None else self.calculer_temps()
        self.cout = self.calculer_cout()

    def calculer_distance(self):
        x1, y1 = self.origine.coord_x, self.origine.coord_y
        x2, y2 = self.destination.coord_x, self.destination.coord_y
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def calculer_temps(self):
        return self.distance / 50  # 50 km/h

    def calculer_cout(self):
        return self.distance * 0.10  # Coût du km

    def __repr__(self):
        return f"Trajet: {self.origine} -> {self.destination}, Distance: {self.distance:.2f} km, Temps: {self.temps:.2f}h, Coût: {self.cout:.2f} AC"
    


def simuler_evolution(camions, timemax):  # camions représente la liste des camions
    time=0
    while time<timemax:
        for camion in camions:
            analyse(temps)
            remplissage(camion)
        time+=1

