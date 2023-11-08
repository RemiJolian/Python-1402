# from the file that exist in current folder
from work_place import WorkPlace, Consts

#class School
class School(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = int((self.level) ** 0.5)

    def calc_costs(self):
        self.costs = Consts.BASE_PLACE_COST * int((self.level) ** 0.5)
        return int(self.costs)