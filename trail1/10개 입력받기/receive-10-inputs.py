arr = list(map(int, input().split()))

no_zero = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    else:
        no_zero += i
        cnt += 1

average = no_zero / cnt

print(f"{no_zero} {average:.1f}")