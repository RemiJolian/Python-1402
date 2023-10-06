n, x, y = input().split()
n, x, y = int(n), int(x), int(y)
for i in range(n // x + 1):
    if (n - i * x) % y == 0:
        print(i, (n - i * x) // y)
        break
else:
    print(-1)