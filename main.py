"""
This is a sample module.

It demonstrates the usage of various transport classes.
"""

from modules.trolleybus import Trolleybus
from modules.car import Car
from modules.motorcycle import Motorcycle
from modules.bike import Bike
from managers.transport_manager import TransportManager
from decorators import *
from managers.set_manager import SM

@logged(Exception, mode='file')
def main():
    """
    Entry point of the program.
    """
    transport_manager = TransportManager()
    transport_manager.add_transports(
        Bike(0,0,['road11','road2'],0,False),
        Bike(0,0,['road11','road2'],0,False),
    )

    for transport in transport_manager.transports:
        print(transport)

    sm = SM(transport_manager)
    

if __name__ == "__main__":
    main()
