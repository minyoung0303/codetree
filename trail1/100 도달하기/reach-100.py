n = int(input())

arr = [1, n]

while True:
    next_val = arr[-1] + arr[-2]
    arr.append(next_val)

    if next_val >= 100:
        break

print(*arr)