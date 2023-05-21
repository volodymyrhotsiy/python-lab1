from modules.Transport import Transport

class Bike(Transport):
    def __init__(self, id=0, max_speed=0, number_of_gears=0, has_pet_bucket=False):
        super().__init__(id, max_speed)
        self.number_of_gears = number_of_gears
        self.has_pet_bucket = has_pet_bucket

    def attach_pet_bucket(self):
        self.has_pet_bucket = True  

    def __str__(self):
        return f"id: {self.id}, max_speed: {self.max_speed},"\
                f" number_of_gears: {self.number_of_gears}, has_pet_bucket: {self.has_pet_bucket}"
    
    def accelerate(self):
        pass     