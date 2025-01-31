class bottle:

    def __init__(self, etat, lieu, type_lieu):

        if etat < 0 or etat > 1:
            raise ValueError("L'état doit être un entier entre 0 et 1.") # Vérification que l'état est entre 0 et 1

        self.etat = etat
        self.lieu = lieu
        self.type_lieu = type_lieu
    
    def afficher_info(self):

        if self.etat == 0:
            etat_bouteille = "vide"
        elif self.etat == 1:
            etat_bouteille = "pleine"
        else:
            etat_bouteille = f"{self.etat * 100}% pleine"


        print(f"bottle: {etat_bouteille} - {self.lieu} - {self.type_lieu}")
        