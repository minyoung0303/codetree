n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(n * i + j + 1, end=" ")
        print()
    else:
        for j in range(n * i + n, n * i, -1):
            print(j, end=" ")
        print()