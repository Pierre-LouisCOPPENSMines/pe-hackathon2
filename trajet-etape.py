def simuler_evolution(camions, timemax):  # camions représente la liste des camions
    time=0
    t=[camion.time for camion in camions]
    while time<timemax:
        for camion in camions:
            analyse(temps)
            remplissage(camion)
        time+=1

