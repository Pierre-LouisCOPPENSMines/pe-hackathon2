import pandas as pd

L_init=[[0,0]for i in range(100)]
print(L_init)

#créer une fonction pour tout mettre à jour 


#state: contient 
class Truck:
    def __init__ (self, coord,state:str,id,empty_bottles,filled_bottles):
        self.coord=coord
        self.state=state
        self.id=id
        self.empty_bottle=empty_bottles
        self.filled_bottles=filled_bottles




#créer une f
class Trucks:
    def __init__(self, L_init):
        L_trucks=[]
        for index,coord in L_init:
            truck=Truck(coord,index,"park",0)
            L_trucks.append(truck)
        self.trucks=L_trucks
    def update(L_trucks,self):
        self.trucks=L_trucks
    def motion(L_id,self):
        for id in L_id:
            i=0
            L_trucks=self.trucks
            while id!=L_trucks[i].id:
                i+=1
            L_trucks[i].state=1
        self.update(L_trucks)
    def stop(L_id,self):
        for id in L_id:
            i=0
            L_trucks=self.trucks
            while id!=L_trucks[i].id:
                i+=1
            L_trucks[i].state=0
        self.update(L_trucks)
#contient la liste des étapes 
    def load(L:list):

#on donne en entrée une liste composé de tuple avec les identifiants des camions remplis et le nombre de bouteilles que l'on met