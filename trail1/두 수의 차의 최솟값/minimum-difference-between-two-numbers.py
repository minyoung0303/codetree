n = int(input())
a = list(map(int, input().split()))
min_val = a[1] - a[0]

for i in range(n):
    for j in range(n):
        if i != j and a[j] > a[i] and a[j] - a[i] < min_val:
            min_val = a[j] - a[i]
    
print(min_val)