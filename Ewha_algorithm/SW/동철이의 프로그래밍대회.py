t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = []
    for k in range(n):
        a.append(list(map(int,input().split())))
    result = []
    for l in range(n):
        total = 0
        for s in range(m):
            if a[l][s] == 1:
                total+=1
        result.append([l,total])
    p,score = 0,0
    if len(result) == 1:
        max_s = result[0][1]
    else:
        max_s = max(result[:][1])
    for r in range(n):
        if result[r][1]>=max_s:
            p+=1
    print(p,max_s)
