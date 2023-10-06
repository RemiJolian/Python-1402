#arr = list(map(int,input().split()))
#n = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 12
L = 0
R = len(arr)
mid = 0

while L < R:
  mid = (R + L) // 2
  if arr[mid] == n:
    L = mid
    break
  elif arr[mid] < n:
    L = mid
  elif arr[mid] > n:
    R = mid
if arr[L] == n:
  print('yes')
else:
  print('No')