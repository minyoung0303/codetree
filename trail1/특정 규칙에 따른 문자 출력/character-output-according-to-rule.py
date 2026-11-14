n = int(input())

for i in range(2 * n - 1):
    if i < n:
        for j in range(n - 1 - i):
            print(" ", end=' ')
        for j in range(i + 1):
            print("@", end=' ')
        print()
    else:
        i -= n
        for j in range(n - 1 - i):
            print("@", end=' ')
        print()