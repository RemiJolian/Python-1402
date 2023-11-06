# import 2 file
from flying_vehicle import FlyingVehicle
from ground_vehicle import GroundVehicle
class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        #super().__init__(self, name, price, number_of_seats, max_speed, number_of_wheels, steering_wheel)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        super().__init__(**kwargs)

class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

