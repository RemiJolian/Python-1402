# YOUR IMPORTS GOES HERE
from person import Person, Consts


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self):
        self.price = int(Consts.BASE_PRICE[self.job] - (self.age - Consts.MIN_AGE)* Consts.AGE_MUL)
        return self.price

    def calc_life_cost(self):
        self.costs = int(Consts.BASE_COST[self.job] + ((self.age - Consts.MIN_AGE) * Consts.AGE_MUL))
        return self.costs

    def calc_income(self):
        self.income = int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] - (self.age - Consts.MIN_AGE)* Consts.AGE_MUL)
        return self.income