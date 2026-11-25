new_arr = [0 for _ in range(4)]

for _ in range(3):
    a, b = input().split()
    b = int(b)

    if a == "Y":
        if b >= 37:
            new_arr[0] += 1
        else:
            new_arr[2] += 1
    else:
        if b >= 37:
            new_arr[1] += 1
        else:
            new_arr[3] += 1

print(*new_arr, end=" ")

if new_arr[0] >= 2:
    print("E", end=" ")