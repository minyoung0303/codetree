n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

su = False

for i in range(n1 - n2 + 1):
    if arr_a[i:i + n2] == arr_b:
        su = True

if su == True:
    print("Yes")
else:
    print("No")