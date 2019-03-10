alist = [[] for _ in range(2500)]
for i in range(int(input())):
    s = list(map(str,input()))
    result = "#"+str(i+1)
    c = 0
    for j in range(len(s)):
        total = 0
        Isit = True
        if s[0] != 'c':
            total = -1
            break
        if s[j] == 'c':
            if j == 0:
                alist[c].append('c')
                continue
            else:
                for k in range(c+1):
                    if alist[k][-1] == 'k':
                        alist[k].append('c')
                        Isit = False
                        break
                if Isit == True:
                    c+=1
                    alist[c].append('c')
                    continue
        if s[j] == 'r':
            for aa in range(c+1):
                if alist[aa][-1] == 'c':
                    alist[aa].append('r')
                    Isit = False
                    break
            if Isit == True:
                total = -1
                break
        if s[j] == 'o':
            for aa in range(c+1):
                if alist[aa][-1] == 'r':
                    alist[aa].append('o')
                    Isit = False
                    break
            if Isit == True:
                total = -1
                break
        if s[j] == 'a':
            for aa in range(c+1):
                if alist[aa][-1] == 'o':
                    alist[aa].append('a')
                    Isit = False
                    break
            if Isit == True:
                total = -1
                break
        if s[j] == 'k':
            for aa in range(c+1):
                if alist[aa][-1] == 'a':
                    alist[aa].append('k')
                    Isit = False
                    break
            if Isit == True:
                total = -1
                break
    for oo in range(c+1):
        if alist[oo][-1] != 'k':
            total = -1
            break
    if total == -1 :
        print(result,total)
    else:
        print(result,c+1)

