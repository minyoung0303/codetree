n = int(input())

arr = list(map(float, input().split()))
total = 0

for i in arr:
    total += i

average = total / n

if average >= 4.0:
    print(f"{average:.1f}")
    print("Perfect")
elif average >= 3.0:
    print(f"{average:.1f}")
    print("Good")
else:
    print(f"{average:.1f}")
    print("Poor")