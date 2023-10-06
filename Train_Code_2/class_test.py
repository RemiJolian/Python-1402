class Books():
    def __init__(self, author, title):    
        self.author = author
        self.title = title
    def info(self):
        print(self.title + ':' +self.author )
b1 = Books('Hafez','divan')
b1.info()
print()

print('----example 2----')       

class Student:
    def __init__(self, name, score):
        self.d = {}
        self.d['name'] = name
        self.d['score'] = score
    def get_stu(self):
        return self.d
obj1 = Student('Baran', 19)
obj2 = Student('Mahoor', 18)
lst = []
lst.append(obj1.get_stu())
lst.append(obj2.get_stu())
print(lst)

print()
print('--------------')
print()

class Circle:
    def __iniabct__(self,r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14
obj1 = Circle(5)
s = obj1.area()
print(s)


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