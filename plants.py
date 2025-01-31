class Plants:
    """Class that regroup the factories."""

    def __init__(self, factories: list["Plant"]):
        self._plants=factories

class Plant:
    """Class that define a factorie."""

    def __init__(self, coord:tuple, capacity:int, init:int, refill:int, plants_id:int):
        self._coord=coord
        self._capacity=capacity
        self._init=init
        self._refill=refill
        self._plants_id=plants_id
