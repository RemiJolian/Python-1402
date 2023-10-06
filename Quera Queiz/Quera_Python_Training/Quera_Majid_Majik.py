N = int(input())
arr = list(map(int, input().split()))
counter = [0] * max(arr)
min_c = 100
for i in range(N):
    #color = arr[i]
    counter[arr[i] - 1] += 1
for i in range(len(counter)):
    if 0 < counter[i] < min_c:
        min_c = counter[i]
        ans = i + 1
print(ans)