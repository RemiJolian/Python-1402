#n , m = map(int,input().split())

n = 2
m = 2
l1 = [[1, 1],[2, 2]]
l2 = [[3, 3], [4, 4]]
l3 = []
k = 0
#for i in range (0,n):
    #l1.append(list(map(int,input().split())))
#for i in range(n):
      #l2.append(list(map(int,input().split())))

for i in range(0,n):
  for j in range(0,m):
   l3[i][j] = l1[i][j]+l2[i][j]
   

print(l1)
print(l2)
print(l3)
