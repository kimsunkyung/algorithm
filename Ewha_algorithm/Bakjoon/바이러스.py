n = int(input())
t = int(input())
a = []
check = [0]*n
check[0] = 1
for i in range(t):
    m,n= map(int,input().split())
    a.append([m,n])
a.sort()
i = 0
print(a)
while i<t:
    if check[a[i][0]-1] == 1:
        if check[a[i][0] - 1] == 1:
            if check[a[i][1]-1] != 1:
                check[a[i][1]-1] = 1

    if check[a[i][1]-1] == 1:
        if check[a[i][1] - 1] == 1:
            if check[a[i][0] - 1] != 1:
                check[a[i][0] - 1] = 1
    i+=1

result = 0
for i in check:
    if i == 1:
        result+=1
print(result-1)



