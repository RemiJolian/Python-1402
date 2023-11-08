# YOUR IMPORTS GOES HERE
from person import Consts


class Worker(...):
    def __init__(self, name, age):
        def __init__(self, name, age):
        super().__init__(name, age)
	self.job = "worker

    def get_price(self):
        self.price = int(Consts.BASE_PRICE[self.job] * (Consts.MINE_AGE/self.age)
	return self.price


    def calc_life_cost(self):
        self.cost = int(Consts.BASE_COST[self.job] * (self.age/Consts.MINE_AGE)
	return self.costs

    def calc_income(self):
        pass