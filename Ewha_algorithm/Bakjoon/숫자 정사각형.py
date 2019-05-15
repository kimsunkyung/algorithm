n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input())))
min_nm = min(n,m)-1
result = False

while True:
    for k in range(n):
        for j in range(m):
            if k+min_nm<n and j+min_nm<m:
                if a[k][j] == a[k][j+min_nm] == a[k+min_nm][j] == a[k+min_nm][j+min_nm]:
                    result = True
        if result ==True:
            break
    if result == True:
        break
    min_nm-=1

min_nm+=1
print(min_nm*min_nm)