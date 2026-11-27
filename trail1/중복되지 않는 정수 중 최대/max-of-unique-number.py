n = int(input())
nums = list(map(int, input().split()))
unique = []

for i in nums:
    if nums.count(i) == 1:
        unique.append(i)
    
if len(unique) == 0:
    print(-1)
else:
    print(max(unique))