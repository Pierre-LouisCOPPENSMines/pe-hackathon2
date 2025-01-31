L_type=["plant","factory"]
L_init=[(0,"plant") for i in range (10)]+[(0,"factory") for i in range (10)]


class Step:
    def __init__(self, id, type):
        self.type=type
        self.id=id


class Route:
    def __init__(self,L_init):
        L_step1=[]
        L_step=[]
        for step1 in L_init:
            step=Step(step1[0],step1[1])
            L_step.append(step)
        L_step1.append(L_step)
        self.route=L_step1
    def update(self,L_step):
        L_route=self.route
        L_route.append(L_step)
        self.route=L_route




import random
def trajet():
    route1=Route(L_init)
    for i in range(10):
        nb_plants=0
        nb_clients=0
        L_id_plants=[]
        L_id_clients=[]
        for element in route1.route[-1]:
            if element.type=="plant":
                nb_plants+=1
                L_id_plants.append(element.id)
            if element.type=="client":
                nb_clients+=1
                L_id_clients.append(element.id)
        L_plants=random.sample(range(101), nb_clients)
        L_clients=random.sample(range(101), nb_plants)
        L_step=[]
        for id,index in enumerate (L_id_plants):
            step=Step(id,L_clients[index])
            L_step.append(step)
        for id,index in enumerate (L_id_clients):
            step=Step(id,L_plants[index])
            L_step.append(step)
        route1.update(L_step)
        

trajet()

            
