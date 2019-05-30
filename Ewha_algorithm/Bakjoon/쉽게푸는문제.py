a = [0]
for i in range(1,50):
    x = [i]*i
    a.extend(x)

f,l = map(int,input().split())
total = 0
for k in range(f,l+1):
    total+=a[k]
print(total)
