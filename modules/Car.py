from modules.transport import Transport


class Car(Transport):
    """
    This is a class representing a Car.
    """

    def __init__(self, car_id=0, max_speed=0, roads_set=None, num_of_doors=0, trunk_volume=0, max_overload=0):
        """
        Initialize a Car object.

        Args:
            car_id (int): The ID of the car.
            max_speed (int): The maximum speed of the car.
            roads_set (set): Set of roads
            num_of_doors (int): The number of doors the car has.
            trunk_volume (int): The trunk volume of the car.
            max_overload (int): The maximum overload capacity of the car.
        """
        super().__init__(car_id, max_speed, roads_set)
        self.num_of_doors = num_of_doors
        self.trunk_volume = trunk_volume
        self.max_overload = max_overload

    def __str__(self):
        """
        Return a string representation of the car.
        """
        return f"car_id: {self.transport_id}, max_speed: {self.max_speed}," \
               f" num_of_doors: {self.num_of_doors}, trunk_volume: {self.trunk_volume}," \
               f" max_overload: {self.max_overload}"

    def accelerate(self):
        """
        Accelerate the car.
        """