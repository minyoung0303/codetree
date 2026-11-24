n = int(input())
cnt = 0

for i in range(n):
    arr = list(map(int, input().split()))
    total = 0

    for i in arr:
        total += i
    
    average = total / len(arr)

    if average >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)