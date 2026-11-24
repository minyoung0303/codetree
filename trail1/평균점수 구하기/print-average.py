arr = list(map(float, input().split()))
total = 0
average = 0

for i in arr:
    total += i
    
average = total / len(arr)

print(f"{average:.1f}")