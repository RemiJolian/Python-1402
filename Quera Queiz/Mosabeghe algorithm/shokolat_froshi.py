b, c = map(int,input().split())
n_array = list(map(int,input().split()))
n = len(n_array)
flage = False
for i in range(n):
    for j in range(n):
       if (n_array[i] + n_array[j]) % c == 0 and (i != j):
         flage = True
         break
if flage or n_array == [0]:
  print('YES')
else:
  print('NO')