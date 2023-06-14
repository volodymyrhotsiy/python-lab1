from modules.transport import Transport


class Bike(Transport):
    """
    This is a class representing a Bike.
    """

    def __init__(self, transport_id=0, max_speed=0, roads_set=None, number_of_gears=0, has_pet_bucket=False):
        """
        Initialize a Bike object.

        Args:
            id (int): The ID of the bike.
            max_speed (int): The maximum speed of the bike.
            roads_set (set): Set of roads
            number_of_gears (int): The number of gears the bike has.
            has_pet_bucket (bool): Whether the bike has a pet bucket or not.
        """
        super().__init__(transport_id, max_speed,roads_set)
        self.number_of_gears = number_of_gears
        self.has_pet_bucket = has_pet_bucket

    def attach_pet_bucket(self):
        """
        Attach a pet bucket to the bike.
        """
        self.has_pet_bucket = True

    def __str__(self):
        """
        Return a string representation of the bike.
        """
        return f"id: {self.transport_id}, max_speed: {self.max_speed}," \
               f" number_of_gears: {self.number_of_gears}, has_pet_bucket: {self.has_pet_bucket}"

    def accelerate(self):
        """
        Accelerate the bike.
        """