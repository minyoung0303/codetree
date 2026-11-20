n = int(input())
num = 2

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        if num >= 8:
            num = 2
        else:
            num += 2
    print()