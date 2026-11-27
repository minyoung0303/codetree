arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]

for i in arr:
    if i == 999 or i == -999:
        print(max_val, min_val)
        break
    elif i > max_val:
        max_val = i
    elif i < min_val:
        min_val = i
    else:
        continue