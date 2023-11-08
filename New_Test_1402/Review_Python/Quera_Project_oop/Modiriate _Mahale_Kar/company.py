# from the file that exist in current folder
from work_place import WorkPlace, Consts

#class Company
class Company(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "company"

    def calc_capacity(self):
        self.capacity = int(self.level)

    def calc_costs(self):
        self.costs = Consts.BASE_PLACE_COST * self.level
        return int(self.costs)