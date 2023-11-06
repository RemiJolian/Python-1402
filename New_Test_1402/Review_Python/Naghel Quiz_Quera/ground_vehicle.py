from vehicle import Vehicle
class GroundVehicle(Vehicle):
    def __init__(self, number_of_wheels, steering_wheel, **kwargs):
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel
        super().__init__(**kwargs)