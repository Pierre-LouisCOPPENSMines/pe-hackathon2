class Trajet:
    def __init__(self, origine, destination, camion, distance=None, temps=None):

        self.origine = origine
        self.destination = destination
        self.camion = camion
        self.distance = distance if distance is not None else self.calculer_distance()
        self.temps = temps if temps is not None else self.calculer_temps()
        self.cout = self.calculer_cout()

    def calculer_distance(self):
        """Calcul la distance entre deux lieux."""
        x1, y1 = self.origine.coord_x, self.origine.coord_y
        x2, y2 = self.destination.coord_x, self.destination.coord_y
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def calculer_temps(self):
        """Calcul le temps de trajet entre deux lieux."""
        return self.distance / 50  # 50 km/h

    def calculer_cout(self):
        """Calcule le prix d'un trajet."""
        return self.distance * 0.10  # Coût du km

    def __repr__(self):
        return f"Trajet: {self.origine} -> {self.destination}, Distance: {self.distance:.2f} km, Temps: {self.temps:.2f}h, Coût: {self.cout:.2f} AC"
    


def simuler_evolution(camions, nbheures):  # camions représente la liste des camions
    """Ebauche d'une fonction non utilisée par la suite. """
    for heure in range(nbheures):       # on avance dans le temps
        for camion in camions:
            camion.avancer_une_heure()  # Chaque camion avance d'une heure et fait ses opérations de chargement et déchargement

            # Exemple de déplacement
            trajet = Trajet(camion.state, 'client', camion)     # on donne à chaque camion sa prochaine destination 
            camion.ajouter_etape('depart', 'client', heure)     # on ajoute cette destination à la liste de passage de ce camion si l'on souhaite par la suite faire des représenation graphique ou de l'analyse de donnée de nos camions