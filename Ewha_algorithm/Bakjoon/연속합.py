n = int(input())
a = [0]+list(map(int,input().split()))
result = [a[0]]

for i in range(1,n+1):
    result.append(max(result[i-1]+a[i],a[i]))
print(max(result[1:]))
