#Quera_Payda kon Prob
n, q = map(int,input().split())
array1 = list(map(int,input().split()))
print(array1)
L = 0
R = len(array1)
for i in range(q):
   s, a = map(str,input().split())
   a = int(a)
   print('a:',a)
   while L < R:
      m = (R + L) // 2
      print('mid_index:', m)
      if a == array1[m]:
           L = 0
           R = len(array1)
           break
      elif a > array1[m]:
           L = m + 1
      elif a < array1[m]:
           R = m
   if array1[m] == a:
       print('a in Array :1')
   else:
       print('a in array:0')
