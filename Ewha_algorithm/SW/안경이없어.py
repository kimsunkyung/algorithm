a_dict = {'A':1,'D':1,'O':1,'P':1,'Q':1,'R':1
,'C':2,'E':2,'F':2,'G':2,'H':2,'I':2,'J':2,'K':2,
'L':2,'M':2,'N':2,'S':2,'T':2,'U':2,'V':2,'W':2,'X':2,'Y':2,'Z':2,
'B':3}

for i in range(int(input())):
    result = "#"+str(i+1)
    flag = "SAME"
    a,b = map(str,input().split())
    if len(a)!=len(b):
        flag = "DIFF"
        print(result,flag)
    else:
        for k in range(len(a)):
            if a_dict[a[k]] != a_dict[b[k]]:
                flag = "DIFF"
                break
        print(result,flag)