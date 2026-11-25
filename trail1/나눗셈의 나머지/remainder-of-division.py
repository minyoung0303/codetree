arr = list(map(int, input().split()))
total = 0
mod = [0 for _ in range(10)]

while True:
    if arr[0] <= 1:
        break
    else:
        mod[arr[0]%arr[1]] += 1
        arr[0] = arr[0] // arr[1]

for i in mod:
    total += i ** 2

print(total)