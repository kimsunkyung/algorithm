import sys
n = int(sys.stdin.readline())
a = []
for k in range(n):
    p,q = list(map(int,sys.stdin.readline().split()))
    a.append((q,p))
a.sort()
min_n,total = 0,0

for i in range(len(a)):
    if a[i][1]>=min_n:
        min_n =a[i][0]
        total+=1

print(total)