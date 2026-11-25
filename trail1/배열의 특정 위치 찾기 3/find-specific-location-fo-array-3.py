arr = list(map(int, input().split()))

for i in range(len(arr)):
    total = 0
    if arr[i] == 0:
        total = arr[i - 1] + arr[i - 2] + arr[i - 3]
        break

print(total)