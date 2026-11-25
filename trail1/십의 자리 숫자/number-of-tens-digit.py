arr = list(map(int, input().split()))

cnt_arr = [0 for _ in range(10)]

for i in arr:
    if i == 0:
        break
    cnt_arr[i // 10] += 1

for i in range(1, 10):
    print(f"{i} - {cnt_arr[i]}")
            