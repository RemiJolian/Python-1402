def f1 (a):
    d = {'tavan2':a**2,"tavan3":a**3}
    return d
print (f1(2))

print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")

def funczoj (l:list)->list:
    a = []
    for i in l:
        if i % 2 ==0:
         a.append(i)
    return(a)
print (funczoj([1,4,3,5,7,8]))

def f2(l):
    for i in l:
        if i == 5:
            return 200 #here the func stop
    return l
print (f2([2,7,8,5,0]))