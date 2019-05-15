n = int(input())
a = list(map(int,input().split()))
max_total = 0
result = []

for i in range(n):
    if max_total+a[i]>=max_total:
        max_total+=a[i]
        result.append(max_total)
    else:
        max_total = 0
r_total = 0
for k in result:
    if r_total<k:
        r_total = k
print(r_total)
