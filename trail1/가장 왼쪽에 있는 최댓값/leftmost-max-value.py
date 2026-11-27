n = int(input())
a = list(map(int, input().split()))
answer = [1]
max_val = a[0]

for i in range(1, n):
    if a[i] > max_val:
        max_val = a[i]
        answer.append(i + 1)
    
print(*answer[::-1])