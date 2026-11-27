arr = ["L", "E", "B", "R", "O", "S"]
al = str(input())
key = True

for i in range(len(arr)):
    if arr[i] == al:
        print(i)
        key = False
        break
if key:
    print("None")