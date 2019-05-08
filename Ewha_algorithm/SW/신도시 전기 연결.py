import operator

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(str,input().split()))
    b = []
    for p in a:
        b.append(int(p))
    dist = []
    for s in range(len(b)-1):
        dist.append(b[s+1]-b[s])
    kk = 0
    total = 0
    if n ==1:
        total = 0
    else:
        while kk<k:
            index,value = max(enumerate(dist),key=operator.itemgetter(1))
            if kk != k-1:
                dist[index] = 0
            kk += 1
        for jj in range(len(dist)):
            total+=dist[jj]
    print(total)




