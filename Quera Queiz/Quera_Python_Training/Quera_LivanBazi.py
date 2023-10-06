n , x = input().split() # x = L, M, R
ans = x
n = int(n)
for i in range(n):
    r1, r2 = input().split()
    if r1 ==  ans:
        ans = r2
    elif r2 == ans:
        ans = r1
    
print(ans)
