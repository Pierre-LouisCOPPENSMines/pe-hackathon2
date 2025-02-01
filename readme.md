Voici le readme
On présentera ici la composition du GIT 

On a choisi le projet sur les bouteilles de gaz. Pour cela, on a en premier lieu créé différentes classes pour stocker des informations (Truck, Places (qui regroupe les usines de productions et les clients)). On a ensuite essayé d'utiliser des classes trajets, route, bottle. 
On a ensuite essayé d'implémenter une première startégie qui faisait évolué le temps toutes les heures et de faire les modifications qui ont eu lieu pendant cette heure avec un trajet aléatoire pour les camions.
Puis on a essayé de l'améliorer. On a choisit de faire un algorythme glouton par rapport au cout pour choisir le trajet à prendre pour chaque camion lorsqu'il a fini le précédent. On a choisit pour le temps de ne s'arrêter que lorsqu'un camion finit l'un de ses trajets. En utilisant un fonction min sur le temps à partir duquel le prochain camion s'arrêtera. 
Au final, on dispose de nos classes, de nos deux fonctions mais on n'a pas eu le temps de les mettre ensemble. Il manque aussi l'actualisation des stock avec le temps (production et consommation tous les jours) et le déchargement des bouteilles lorsque l'on fait le changement de trajets. 

On a pu assembler les fichiers ensembles et obtenir un résultat dans la soirée suivant le hackaton. Le commit a été effectué le lendemain. 
L'actualisation des stocks n'est toujours pas prise en compte mais il serait désormais possible de l'implémenter. 
