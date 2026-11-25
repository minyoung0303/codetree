arr = list(map(int, input().split()))
new_arr = [0 for _ in range(11)]

for i in arr:
    if i == 0:
        break
    new_arr[i // 10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {new_arr[i]}")