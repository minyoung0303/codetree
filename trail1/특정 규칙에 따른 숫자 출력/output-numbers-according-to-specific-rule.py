n = int(input())
total = 1

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(total, end=" ")
        if total < 9:
            total += 1
        else:
            total = 1
    print()