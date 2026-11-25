arr = list(map(int, input().split()))
odd_val = 0
even_val = 0

for i in range(0, len(arr), 2):
    odd_val += arr[i]

for i in range(1, len(arr), 2):
    even_val += arr[i]

print(abs(odd_val - even_val))