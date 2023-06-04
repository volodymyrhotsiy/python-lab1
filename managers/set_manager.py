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
        try:
            self.transports_roads = [road for transport in transport_manager.transports for road in transport.roads_set]
        except TypeError:
            print('Transport roads_set is empty')  
        self.__current = -1

    

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
        try:
            return self.transports_roads[index]
        except IndexError:
            print('Invalid index')
    

    def __next__(self):
        """
        Get the next road set in SM.

        Returns:
            set: The next road set.

        Raises:
            StopIteration: If there are no more road sets.
        """
        self.__current += 1
        if self.__current >= len(self.transports_roads):
            raise StopIteration
        return self.transports_roads[self.__current]
    