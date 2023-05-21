from abc import ABC, abstractclassmethod

class Transport(ABC):
    def __init__(self,id=0,max_speed=0):
        self.id = id
        self.max_speed = max_speed

    @abstractclassmethod    
    def accelerate(speed):
        pass