class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'mine': 300, 'school': 100, 'company': 200}
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10


class WorkPlace:
    
    instances = []   # static var
    
    def __init__(self, name):
        self.name = name         # name of work_place
        self.level = 1           # level of work_place
        self.expertise = ""  
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self):
        return self.expertise

    def calc(self):
        return -1 * self.calc_costs()

    @staticmethod
    def calc_all():
        total = 0
        for obj in WorkPlace.instances:
            total += obj.calc()
        return total