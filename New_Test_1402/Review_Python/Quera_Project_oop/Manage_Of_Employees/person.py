import math


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'worker': 200, 'teacher': 150, 'engineer': 250}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 800, 'school': 500, 'company': 600},
                   'teacher': {'mine': 400, 'school': 900, 'company': 700},
                   'engineer': {'mine': 1000, 'school': 800, 'company': 900}}
    MIN_AGE = 5
    AGE_MUL = 5


class Person:
    instances = []

    def __init__(self, name, age):
        pass

    def do_level(self, income):
        pass

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        pass

    def get_job(self):
        pass

    def upgrade(self):
        pass

    @staticmethod
    def calc_all():
        pass