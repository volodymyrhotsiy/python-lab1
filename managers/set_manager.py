"""
Module docstring: This module contains the SM class.
"""

class SM:
    """
    Class docstring: Represents an SM object.
    """
    def __init__(self, transport_manager):
        """
        Initialize an SM object.

        Args:
            transport_manager (TransportManager): The TransportManager object to associate with SM.
        """
        self.transport_manager = transport_manager
        self.transports_roads = [transport.roads_set for transport in self.transport_manager.transports]
        self.current = -1
    def __iter__(self):
        """
        Returns the iterator object for SM.

        Returns:
            SM: The iterator object.
        """
        return self
    def __len__(self):
        """
        Get the number of transports' road sets in SM.

        Returns:
            int: The number of transports' road sets.
        """
        return len(self.transports_roads)
    def __getitem__(self, index):
        """
        Get the road set at the specified index.

        Args:
            index: The index of the road set.

        Returns:
            set: The road set at the specified index.
        """
        return self.transports_roads[index]
    def __next__(self):
        """
        Get the next road set in SM.

        Returns:
            set: The next road set.

        Raises:
            StopIteration: If there are no more road sets.
        """
        self.current += 1
        if self.current >= len(self.transports_roads):
            raise StopIteration
        return self.transports_roads[self.current]
