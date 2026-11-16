n = int(input())
k = 9
for i in range(n):
    for j in range(1, n+1):
        print(k + (2*j), end=" ")
    k += 2
    print()