n = int(input())

arr = list(map(int, input().split()))
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)

print(*even[::-1])