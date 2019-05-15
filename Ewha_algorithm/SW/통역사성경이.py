t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    r = "#"+str(i+1)
    result = []
    a = a.strip()
    a = a.replace("!",".")
    a = a.replace('?',".")
    a = a.split(".")

    for j in range(len(a)):
        a[j] = a[j].strip()
        a[j] = a[j].split()

    for k in range(n):
        total = 0
        for o in range(len(a[k])):
            ok = False
            if a[k][o][0].isalpha() and a[k][o][0].istitle():
                for p in range(1,len(a[k][o])):
                    if a[k][o][p].isalpha() == False or a[k][o][p].istitle():
                        ok = True
            else:
                ok = True
            if ok == False:
                total+=1
        result.append(total)

    f_result = ""
    for l in range(len(result)):
        if l ==0:
            f_result = f_result+str(result[l])
        else:
            f_result = f_result+" "+str(result[l])
    print(r,f_result)