n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    q_list = list(map(int, input().split()))

    if q_list[0] == 1:
        print(arr[q_list[1] - 1])
    elif q_list[0] == 2:
        for i in range(len(arr)):
            if arr[i] == q_list[1]:
                print(i + 1)
                break
        else:
            print(0)
    elif q_list[0] == 3:
        print(*arr[q_list[1] - 1:q_list[2]])
    else:
        break

