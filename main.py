"""
This is a sample module.

It demonstrates the usage of various transport classes.
"""

from modules.trolleybus import Trolleybus
from modules.car import Car
from modules.motorcycle import Motorcycle
from modules.bike import Bike
from managers.transport_manager import TransportManager


def main():
    """
    Entry point of the program.
    """
    transport_manager = TransportManager()
    transport_manager.add_transports(
        Trolleybus(),
        Trolleybus(),
        Car(),
        Car(),
        Motorcycle(),
        Motorcycle(),
        Bike(),
        Bike()
    )

    for transport in transport_manager.transports:
        print(transport)



if __name__ == "__main__":
    main()
