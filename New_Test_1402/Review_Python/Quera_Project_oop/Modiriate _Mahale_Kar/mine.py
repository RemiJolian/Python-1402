# from the file that exist in current folder
from work_place import WorkPlace, Consts 

#class School
class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = int((self.level) ** 2)

    def calc_costs(self):
        self.costs = Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
        return int(self.costs)
    