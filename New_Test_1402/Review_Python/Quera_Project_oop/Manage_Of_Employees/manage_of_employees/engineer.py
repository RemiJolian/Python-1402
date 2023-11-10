# YOUR IMPORTS GOES HERE
from person import Person, Consts

class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
	self.job = "engineer"
	

    def get_price(self):
        self.price = int(Consts.BASE_PRICE[self.job] * ((self.Consts.MINE_AGE/self.age) ** 0.5))
	return self.price

    def calc_life_cost(self):
        self.costs = int(Consts.BASE_COST[self.job] * ((self.age/self.Consts.MINE_AGE) ** 0.5))
	return self.costs

    def calc_income(self):
        self.income = int(Consts.BASE_INCOME[self.job] * (self.Consts.MINE_AGE/self.age) ** 0.5)
	return self.income