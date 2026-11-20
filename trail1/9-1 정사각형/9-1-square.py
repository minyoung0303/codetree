n = int(input())
num = 9

for i in range(n):
    for j in range(n):
        print(num, end="")
        if num <= 1:
            num = 9
        else:
            num -= 1
    print()