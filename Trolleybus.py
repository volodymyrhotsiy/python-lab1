class Troleybus:

    instance = None

    def __init__(self,id=0,route_number=0,current_stop=0,max_speed=0,capacity=0,speed=0,passangers=0):
        self.id = id
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.speed = speed
        self.passangers = passangers

    @staticmethod
    def get_instance():
        if not Troleybus.instance:
            Troleybus.instance = Troleybus()
        return Troleybus.instance    

    def stop(self):
        self.speed = 0

    def start(self):
        self.speed = 20

    def add_passanger(self):
        if self.passangers < self.capacity:
            self.passangers += 1

    def remove_passanger(self):
        if self.passangers: self.passangers -= 1  
    
    def __str__(self):
        return f"route_number: {self.route_number}, current_stop: {self.current_stop},"\
                f"max_speed: {self.max_speed}, capacity: {self.capacity},"\
                f"speed: {self.speed}, passangers: {self.passangers}"
    
def main():    
    troleybuses = [Troleybus(22,22,"stop1",60,20,20,0),Troleybus(),Troleybus.get_instance(),Troleybus.get_instance()]
    [print(troleybus) for troleybus in troleybuses]

if __name__ == "__main__":
    main()    