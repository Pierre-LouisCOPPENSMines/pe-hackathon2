class Place:
    """Class that define a place."""

    def __init__(self, coord:tuple, capacity:int, init:int, flow:float, place_id:int, type:str):
        self._coord=coord
        self._capacity=capacity
        self._type = type
        if (self._type == "plant"):
            self._flow=flow
            self._stock= [True for i in range(init)] + [None for i in range(capacity-init)]
        elif (self._type == "client"):
            self._flow=-flow
            self._stock= [False for i in range(init)] + [None for i in range(capacity-init)]
        else: 
            raise ValueError("The type of the place must be either plant or client.")
        self._place_id=place_id 
        
        

        
        
        

