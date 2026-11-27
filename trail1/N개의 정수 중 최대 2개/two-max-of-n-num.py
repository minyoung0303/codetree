n = int(input())
a = list(map(int, input().split()))
max_val = a[0]
max_val2 = a[1]

for i in range(2, n):
    if a[i] >= max_val:
        max_val2 = max_val
        max_val = a[i]
    elif a[i] > max_val2:
        max_val2 = a[i]

print(max_val, max_val2)