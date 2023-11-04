class FlyingVehicle(Vehicle):
    def __init__(self, name, price, number_of_seat, max_speed, fuel, number_of_fins):
        super().__init__(name, price, number_of_seat, max_speed)
        self.fuel = fuel
        self.number_of_fins