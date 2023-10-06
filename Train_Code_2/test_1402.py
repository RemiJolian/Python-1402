s = input()
q = input()

for i in range(len(s)-1):
    flag = True
    for j in range(len(q)-1):
        if i + j <= len(s):
            if s[i+j] != q[j]:
                flage = False
        else:
            flage= False
    if flage is True:
        print(i+1)