arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for i in arr:
    if i >= 250:
        break
    else:
        sum_val += i
        cnt += 1
print(sum_val, f"{sum_val / cnt:.1f}")