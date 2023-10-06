n = int(input())
s =input()
for i in range(1,n):
  print('i prime:',i)
  if s[i] == s[i-1]:
    s = s[:i-1] + s[i+1:]
    print('s:', s)
    print('n:',n)
    print('i:',i)
  n = len(s)
  
    
print(s)