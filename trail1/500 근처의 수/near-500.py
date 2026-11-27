a = list(map(int, input().split()))
max_val = 1
min_val = 1000

for i in a:
    if i > max_val and i < 500:
        max_val = i
    
for i in a:
    if i > 500 and i < min_val:
        min_val = i
    
print(max_val, min_val)