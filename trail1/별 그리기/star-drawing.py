n = int(input())

for i in range(2 * n - 1):
    if i < n:
        for j in range(n - (i + 1)):
            print(' ',end='')
        for j in range(2 * i + 1):
            print('*',end='')
        print()
    else:
        i -= n
        for j in range(i + 1):
            print(' ',end='')
        for j in range(2 * n - 2 * i - 3):
            print('*',end='')
        print()