def simuler_evolution(camions, timemax):  # camions représente la liste des camions
    """Ebauche d'une fonction non utilisée par la suite. """
    time=0
    t=[camion.time for camion in camions]
    while time<timemax:
        for camion in camions:
            analyse(temps)
            remplissage(camion)
        time+=1

