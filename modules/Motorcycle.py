from modules.transport import Transport


class Motorcycle(Transport):
    """
    This is a class representing a Motorcycle.
    """

    def __init__(self, motorcycle_id=0, max_speed=0, roads_set=None, engine_size=0, has_cupcake_holder=False):
        """
        Initialize a Motorcycle object.

        Args:
            motorcycle_id (int): The ID of the motorcycle.
            max_speed (int): The maximum speed of the motorcycle.
            roads_set (set): Set of roads
            engine_size (int): The engine size of the motorcycle.
            has_cupcake_holder (bool): Whether the motorcycle has a cupcake holder or not.
        """
        super().__init__(motorcycle_id, max_speed, roads_set)
        self.engine_size = engine_size
        self.has_cupcake_holder = has_cupcake_holder

    def attach_cupcake_holder(self):
        """
        Attach a cupcake holder to the motorcycle.
        """
        self.has_cupcake_holder = True

    def __str__(self):
        """
        Return a string representation of the motorcycle.
        """
        return f"motorcycle_id: {self.transport_id}, max_speed: {self.max_speed}," \
               f" engine_size: {self.engine_size}, has_cupcake_holder: {self.has_cupcake_holder}"

    def accelerate(self):
        """
        Accelerate the motorcycle.
        """