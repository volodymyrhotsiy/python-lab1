"""
Module docstring: This module contains the TransportManager class.
"""

class TransportManager:
    """
    Class docstring: Manages a collection of transports.
    """

    def __init__(self):
        """
        Initialize a TransportManager object.
        """
        self.transports = []
    def add_transports(self, *transports):
        """
        Adds transports to the collection.

        Args:
            *transports: Variable number of transport objects.
        """
        for transport in transports:
            self.transports.append(transport)
    def remove_transport(self, transport):
        """
        Removes a transport from the collection.

        Args:
            transport: The transport object to remove.
        """
        self.transports.remove(transport)
    def find_all_transport_of_one_type(self, transport_type):
        """
        Finds all transports of a specific type in the collection.

        Args:
            transport_type: The type of transport to search for.

        Returns:
            List: A list of transports matching the specified type.
        """
        return list(filter(lambda x: isinstance(x, transport_type), self.transports))
    def find_all_transport_with_max_speed(self, max_speed):
        """
        Finds all transports with a maximum speed greater than the specified value.

        Args:
            max_speed: The maximum speed value to compare.

        Returns:
            List: A list of transports with maximum speed greater than the specified value.
        """
        return list(filter(lambda x: x.max_speed > max_speed, self.transports))
    def __len__(self):
        """
        Get the length of the TransportManager.

        Returns:
            int: The number of transports in the collection.
        """
        return len(self.transports)
    def __getitem__(self, index):
        """
        Get the transport at the specified index.

        Args:
            index: The index of the transport.

        Returns:
            Transport: The transport object at the specified index.
        """
        return self.transports[index]
    def __iter__(self):
        """
        Iterate over the transports in the collection.

        Returns:
            Iterator: An iterator object over the transports.
        """
        return iter(self.transports)
    def accelerate_all_transports(self):
        """
        Accelerate all transports in the collection.
        """
        for transport in self.transports:
            transport.accelerate()
    def enumerate_all_transports(self):
        """
        Enumerate all transports in the collection.

        Returns:
            Enumerate: An enumerate object over the transports.
        """
        return enumerate(self.transports)
    def pair_all_transports_to_accelerate_function(self):
        """
        Pair all transports with their corresponding accelerate function.

        Returns:
            zip: A zip object containing pairs of transports and their accelerate functions.
        """
        return zip(self.transports, self.accelerate_all_transports())
    def dict_representation_of_transports(self, value_type):
        """
        Get a dictionary representation of the transports.

        Args:
            value_type: The type of value to include in the dictionary.

        Returns:
            dict: A dictionary representation of the transports.
        """
        return {key: value for (key, value) in self.__dict__.items() if isinstance(value, value_type)}
    def is_there_a_transport_with_id(self, transport_id):
        """
        Check if there is a transport with the specified ID in the collection.

        Args:
            transport_id: The ID to search for.

        Returns:
            dict: A dictionary indicating if there are transports matching the ID.
                {'all': True/False, 'any': True/False}
        """
        all_ids_match = all(transport.transport_id == transport_id for transport in self.transports)
        any_id_matches = any(transport.transport_id == transport_id for transport in self.transports)
        return {'all': all_ids_match, 'any': any_id_matches}
