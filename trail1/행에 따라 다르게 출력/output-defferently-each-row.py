n = int(input())
count = 1

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(count, end=" ")
            count += 1
        else:
            count += 1
            print(count, end=" ")
            count += 1
    print()