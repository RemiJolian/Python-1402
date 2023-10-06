N = int(input())
arr = list(map(int, input().split())) # [7, 1, 1, 7, 6]
arr.sort()                # arr = [1, 1, 6, 7, 7]
cols = list(set(arr))     # cols = [1, 2, 6, 7]
cols.sort()
color = arr[0]             # color = 1       
count = arr.count(color)   # count(1) = 2
for x in cols:
	n = arr.count(x)
	if n < count:
		color = x
		count = n
print(color)