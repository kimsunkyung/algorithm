import sys
sys.setrecursionlimit(10000000)
result = []
def go(nlist,i,k,total):
    if nlist[i][1]<=nlist[k][0] and k<n:
        if k+1<n:
            go(nlist, k, k + 1, total + 1)
        else:
            total+=1
            result.append(total)
    if k+1>=n:
        return
    go(nlist,i,k+1,total)

n = int(sys.stdin.readline())
a = []
for k in range(n):
    p,q = list(map(int,sys.stdin.readline().split()))
    a.append((p,q))
for j in range(n-2):
    go(a,j,j+1,1)
max = 0
for qq in result:
    if max<qq:
        max = qq
print(max)