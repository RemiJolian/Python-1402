# YOUR IMPORTS GOES HERE
from person import POerson, Consts


class Worker(Person):
    def __init__(self, name, age):
        def __init__(self, name, age):
        super().__init__(name, age)
	self.job = "worker"

    def get_price(self):
        self.price = int(Consts.BASE_PRICE[self.job] * (Consts.MINE_AGE/self.age))
	return self.price


    def calc_life_cost(self):
        self.costs = int(Consts.BASE_COST[self.job] * (self.age/Consts.MINE_AGE))
	return self.costs

    def calc_income(self):
        self.income = int(Consts.BASE_INCOME[self.job] * (self.age/Consts.MINE_AGE))
	return self.income