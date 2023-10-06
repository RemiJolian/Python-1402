n = int(input())
name_b = ' '
max = 0
for i in range(n):
  name, ekht = map(str,input().split())
  if int(ekht) > max:
    max = int(ekht)
    name_b = name
print (name_b)