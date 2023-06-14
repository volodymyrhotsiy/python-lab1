class TransportManager:
    def __init__(self):
        self.transports = []

    def add_transports(self,*transports):
        for transport in transports:
            self.transports.append(transport)

    def remove_transport(self,transport):
        self.transports.remove(transport)    

    def find_all_transport_of_one_type(self,type):
        return list(filter(lambda x: isinstance(x,type), self.transports))

    def find_all_transport_with_max_speed(self,max_speed):
        return filter(lambda x: x.max_speed > max_speed, self.transports)
    