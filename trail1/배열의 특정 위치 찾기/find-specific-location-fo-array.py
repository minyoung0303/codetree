arr = list(map(int, input().split()))
even_val = 0
third_val = 0

for i in range(1, len(arr), 2):
    even_val += arr[i]

for j in range(2, len(arr), 3):
    third_val += arr[j]

third_avg = third_val / (len(arr)//3)

print(even_val, f"{third_avg:.1f}")