n = int(input())

for i in range(n * 2-1):
    if i < n:
        for j in range(i):
            print(' ',end=' ')
        for j in range(2 * n - 2 * i-1):
            print('*',end=' ')
        print()
    else:
        for j in range(2 * n - i - 2):
            print(' ',end=' ')
        for j in range(2 * i - 2 * n + 3):
            print('*',end=' ')
        print()