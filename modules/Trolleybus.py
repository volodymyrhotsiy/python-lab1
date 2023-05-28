"""
This module defines the Trolleybus class representing a trolleybus.
"""

from modules.transport import Transport


class Trolleybus(Transport):
    """
    This is a class representing a Trolleybus.
    """

    _instance = None

    def __init__(
        self,
        trolleybus_id=0,
        max_speed=0,
        roads_set=None,
        route_number=0,
        current_stop=0,
        capacity=0,
        speed=0,
        passengers=0,
    ):
        """
        Initialize a Trolleybus object.

        Args:
            trolleybus_id (int): The ID of the trolleybus.
            max_speed (int): The maximum speed of the trolleybus.
            roads_set (set): A set of roads the trolleybus can travel on.
            route_number (int): The route number of the trolleybus.
            current_stop (int): The current stop of the trolleybus.
            capacity (int): The capacity of the trolleybus.
            speed (int): The speed of the trolleybus.
            passengers (int): The number of passengers on the trolleybus.
        """
        super().__init__(trolleybus_id, max_speed, roads_set)
        self.route_number = route_number
        self.current_stop = current_stop
        self.capacity = capacity
        self.speed = speed
        self.passengers = passengers

    @staticmethod
    def get_instance():
        """
        Get the instance of the Trolleybus class.

        Returns:
            Trolleybus: The instance of the Trolleybus class.
        """
        if not Trolleybus._instance:
            Trolleybus._instance = Trolleybus()
        return Trolleybus._instance

    def stop(self):
        """
        Stop the trolleybus.
        """
        self.speed = 0

    def start(self):
        """
        Start the trolleybus.
        """
        self.speed = 20

    def add_passenger(self):
        """
        Add a passenger to the trolleybus if there is capacity.
        """
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        """
        Remove a passenger from the trolleybus if there are passengers.
        """
        if self.passengers:
            self.passengers -= 1

    def __str__(self):
        """
        Return a string representation of the trolleybus.
        """
        return f"trolleybus_id: {self.transport_id}, max_speed: {self.max_speed}," \
               f" route_number: {self.route_number}, current_stop: {self.current_stop}," \
               f" capacity: {self.capacity}, speed: {self.speed}," \
               f" passengers: {self.passengers}"

    def accelerate(self):
        """
        Accelerate the trolleybus.
        """
