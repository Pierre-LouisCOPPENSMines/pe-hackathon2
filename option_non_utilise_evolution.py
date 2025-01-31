def simuler_evolution(camions, nbheures):  # camions représente la liste des camions
    for heure in range(nbheures):       # on avance dans le temps
        for camion in camions:
            camion.avancer_une_heure()  # Chaque camion avance d'une heure et fait ses opérations de chargement et déchargement

            # Exemple de déplacement
            trajet = Trajet(camion.state, 'client', camion)     # on donne à chaque camion sa prochaine destination 
            camion.ajouter_etape('depart', 'client', heure)     # on ajoute cette destination à la liste de passage de ce camion si l'on souhaite par la suite faire des représenation graphique ou de l'analyse de donnée de nos camions