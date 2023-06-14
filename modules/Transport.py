from abc import ABC, abstractmethod


class Transport(ABC):
    """
    This is an abstract base class representing a Transport.
    """

    def __init__(self, transport_id=0, max_speed=0, roads_set=None):
        """
        Initialize a Transport object.

        Args:
            transport_id (int): The ID of the transport.
            max_speed (int): The maximum speed of the transport.
            roads_set (set): A set of roads the transport can travel on.
        """
        self.transport_id = transport_id
        self.max_speed = max_speed
        self.roads_set = roads_set

    @abstractmethod
    def accelerate(self):
        """
        Abstract method to accelerate the transport.
        """

    def __iter__(self):
        """
        Returns an iterator object for iterating over the roads the transport can travel on.

        Returns:
            iterator: An iterator object.
        """
        return iter(self.roads_set)
