n = int(input())
cnt = 0
i = 1
prob = []

while cnt < 2:
    num = n * i
    prob.append(num)

    if num % 5 == 0:
        cnt += 1
        
    i += 1

print(*prob)