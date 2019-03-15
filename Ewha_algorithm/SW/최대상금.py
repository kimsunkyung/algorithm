T = int(input())

for t in range(T):
    inp = input().split()

    arr = []
    val = inp[0]
    M = int(inp[1])

    for i in range(len(val)):
        arr.append(int(val[i]))

    max_arr = [[] for rows in range(2)]
    N = len(arr)
    num = 0

    for i in range(N - 1):
        if (arr[i] != max(arr[i:N])):
            for j in range(N - 1, i, -1):
                if (arr[j] == max(arr[i:N])):
                    if (max(arr[i:N]) == max(arr)):
                        num = num + 1
                        max_arr[0].append(arr[i])
                        max_arr[1].append(j)
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    M = M - 1
                    break
        if (M == 0):
            break

    if (num > 1):
        max_arr[0].sort()
        for i in range(len(max_arr[0])):
            arr[max_arr[1][i]] = max_arr[0][i]

    if (M != 0):
        for i in range(N):
            if (arr.count(arr[i]) > 1):
                M = 0
        while (M > 0):
            temp = arr[len(arr) - 2]
            arr[len(arr) - 2] = arr[len(arr) - 1]
            arr[len(arr) - 1] = temp
            M = M - 1

    answer = ""
    for i in range(len(arr)):
        answer += str(arr[i])

    print("#%s %s" % (t + 1, answer))