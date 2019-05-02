n = int(input())
a,result = [],[]
for i in range(n):
    a.append(int(input()))

result.append(a[0])
result.append(a[0]+a[1])
result.append(max(a[2]+a[0], a[2]+a[1]))

for i in range(3,n):
    result.append(max(a[i]+result[i-2],a[i]+a[i-1]+result[i-3]))


print(result[-1])
