arr = list(map(int, input().split()))

for i in range(2, 10):
    next_val = arr[-1] + 2 * arr[-2]
    arr.append(next_val)

print(*arr)