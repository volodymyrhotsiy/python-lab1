from modules.Transport import Transport

class Trolleybus(Transport):

    _instance = None

    def __init__(self, id=0,max_speed=0, route_number=0, current_stop=0, capacity=0, speed=0, passengers=0):
        super().__init__(id, max_speed)
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.speed = speed
        self.passengers = passengers

    @staticmethod
    def get_instance():
        if not Trolleybus._instance:
            Trolleybus._instance = Trolleybus()
        return Trolleybus._instance
    
    def stop(self):
        self.speed = 0

    def start(self):
        self.speed = 20

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        if self.passengers:
            self.passengers -= 1

    def __str__(self):
        return f"id: {self.id}, max_speed: {self.max_speed},"\
                f" route_number: {self.route_number}, current_stop: {self.current_stop},"\
                f" capacity: {self.capacity}, speed: {self.speed},"\
                f" passangers: {self.passengers}"
    
    def accelerate(self):
        pass

