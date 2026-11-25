n = int(input())
arr = list(map(int, input().split()))

cnt_arr = [0 for _ in range(10)]

for i in arr:
    if 1 <= i <= 9:
        cnt_arr[i] += 1


for i in range(1, 10):
    print(cnt_arr[i])