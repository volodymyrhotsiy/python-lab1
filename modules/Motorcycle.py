from modules.Transport import Transport

class Motorcycle(Transport):
    def __init__(self, id=0, max_speed=0, engine_size=0, has_cupcake_holder=False):
        super().__init__(id, max_speed)
        self.engine_size = engine_size
        self.has_cupcake_holder = has_cupcake_holder

    def attach_cupcake_holder(self):
        self.has_cupcake_holder = True

    def __str__(self):
        return f"id: {self.id}, max_speed: {self.max_speed},"\
                f" engine_size: {self.engine_size}, has_cupcake_holder: {self.has_cupcake_holder}"
    
    def accelerate(self):
        pass
