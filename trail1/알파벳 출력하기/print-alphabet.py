n = int(input())
num = 65

for i in range(n):
    for j in range(i + 1):
        print(chr(num), end="")
        if chr(num) == "Z":
            num = 65
        else:
            num += 1
    print()