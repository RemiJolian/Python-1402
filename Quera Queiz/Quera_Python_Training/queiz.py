p, d = map(int,input().split())
i = 1
m = i * d
while m % p > (p/2):
    i = i + 1

print(m)