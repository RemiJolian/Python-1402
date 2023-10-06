
class C:
    def __init__(self, age, name):
        self.s = ''
        self.age = age 
        self.n = name 
        
    def get(self):
        self.s = input('input')
        
    def show(self):
        print(self.s.upper())
        print(self.age+ 1)

kid_name = 'Baran'     
obj1 = C(3, kid_name)
obj1.get()
obj1.show()