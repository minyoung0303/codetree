n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(65 + i * n + j), end="")
    print()