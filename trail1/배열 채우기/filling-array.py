arr = list(map(int, input().split()))

no_zero = []

for i in arr:
    if i == 0:
        break
    else:
        no_zero.append(i)

print(*no_zero[::-1])