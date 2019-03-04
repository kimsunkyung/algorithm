a,result = [],[]
k=1
ok = True
for i in range(int(input())):
    n = int(input())
    while k<=n:
        a.append(k)
        result.append('+')
        k+=1
    if a[-1] == n:
        a.pop()
        result.append('-')
    else:
        ok = False
if ok == True:
    for r in result:
        print(r)
else:
    print("NO")



