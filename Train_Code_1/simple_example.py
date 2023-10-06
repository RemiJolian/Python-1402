num = [1,2,5,7,4,9,22]
add_num =[]
for i in num:
    if i%2 == 0:
        add_num.append(i)
print(add_num)        

a=[2,3] * 2  # =[2,3,2,3]

b={ 'tehran':11, 'sirjan':22,'laar':44}
for k,v in b.items():
    print(k,v)

def power(a:int)-> int:
    d = {"tavan 2":a**2,'tavan 3':a**3}
    return d
print(power (10))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def evenNum(l:list):
    enum=[]
    for i in l:
        if i % 2 == 0:
            enum.append(i)
    return (enum)
print(evenNum([3,4,5,6,7,8,9]))


