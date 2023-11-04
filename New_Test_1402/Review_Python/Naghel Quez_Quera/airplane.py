class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, name, price, number_of_seat, max_speed, fuel, number_of_fins, number_of_wheels, steering_wheel, airline, number_of_crew, captain):
        super().__init__(name, price, number_of_seat, max_speed, fuel, number_of_fins, number_of_wheels, steering_wheel)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain

class B707(Airplane):
    def __init__(self, name, price, number_of_seat, max_speed, fuel, number_of_fins, number_of_wheels, steering_wheel, airline, number_of_crew, captain):
        super().__init__(name, price, number_of_seat, max_speed, fuel, number_of_fins, number_of_wheels, steering_wheel, airline, number_of_crew, captain)
