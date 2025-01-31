def simuler_evolution(camions, timemax):  # camions représente la liste des camions
    time=0
    while time<timemax:
        for camion in camions:
            analyse(temps)
            remplissage(camion)
        time+=1

