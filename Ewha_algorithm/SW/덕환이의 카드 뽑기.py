t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = []
    for q in range(n):
        a.append(q+1)
    while len(a) != 1:
        for j in range(k):
            a.append(a[0])
            del a[0]
        del a[0]
    print(a[0])
