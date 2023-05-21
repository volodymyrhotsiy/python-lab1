from modules.Trolleybus import Trolleybus
from modules.Car import Car 
from modules.Motorcycle import Motorcycle
from modules.Bike import Bike
from managers.TransportManager import TransportManager

def main():
    transport_manager = TransportManager()
    transport_manager.add_transports(Trolleybus(),Trolleybus(),
                                     Car(),Car(),
                                     Motorcycle(),Motorcycle(),
                                     Bike(),Bike())
    for transport in transport_manager.transports:
        print(transport)

if __name__ == "__main__":
    main()    