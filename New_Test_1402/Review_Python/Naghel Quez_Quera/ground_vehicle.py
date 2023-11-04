class GroundVehicle(Vehicle):
    def __init__(self, name, price, number_of_seat, max_speed, number_of_wheels, steering_wheel):
        super().__init__(name, price, number_of_seat, max_speed)
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel