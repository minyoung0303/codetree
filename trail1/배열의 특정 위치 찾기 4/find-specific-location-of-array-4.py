arr = list(map(int, input().split()))
no_zero = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            no_zero += i
            cnt += 1

print(cnt, no_zero)