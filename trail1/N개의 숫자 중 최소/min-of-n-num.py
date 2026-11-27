n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
cnt = 0

for i in a:
    if i < min_val:
        min_val = i
        cnt = 0
    if i == min_val:
        cnt += 1

print(min_val, cnt)