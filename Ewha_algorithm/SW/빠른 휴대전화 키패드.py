t = int(input())
a = [ _ for _ in range(10)]
a[2]=['a','b','c']
a[3]=['d','e','f']
a[4]=['g','h','i']
a[5]=['j','k','l']
a[6]=['m','n','o']
a[7]=['p','q','r','s']
a[8]=['t','u','v']
a[9]=['w','x','y','z']

for i in range(t):
    total = 0
    s,p= map(int,input().split())
    word = list(map(str,input().split()))
    s = str(s)
    str_len = len(s)
    for ss in range(p):
        x_result=True
        for kk in range(str_len):
            if len(word[ss])<=1000000:
                if len(word[ss]) != str_len:
                    x_result = False
                    break
                if not word[ss][kk] in a[int(s[kk])]:
                    x_result = False
        if x_result == True:
            total+=1
        result = "#"+str(i+1)
    print(result,total)


