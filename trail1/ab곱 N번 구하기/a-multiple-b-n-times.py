n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    prob_val = 1
    for j in range(a, b + 1):
        prob_val *= j
    print(prob_val)