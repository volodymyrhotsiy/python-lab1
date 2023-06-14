from modules.Transport import Transport

class Car(Transport):
    def __init__(self, id=0, max_speed=0, num_of_doors=0, trunk_volume=0, max_overload=0):
        super().__init__(id, max_speed)
        self.num_of_doors = num_of_doors
        self.trunk_volume = trunk_volume
        self.max_overload = max_overload

    def __str__(self):
        return f"id: {self.id}, max_speed: {self.max_speed},"\
                f" num_of_doors: {self.num_of_doors}, trunk_volume: {self.trunk_volume},"\
                f" max_overload: {self.max_overload}"
    
    def accelerate(self):
        pass