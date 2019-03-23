for i in range(int(input())):
    s = "#"+str(i+1)
    l,r = map(int,input().split())
    total = 0
    while l<=r:
        for k in range(1,l+1):
            if l%k==0 and k%2 != 0:
                total+=k
        l+=1
    print(s,total)
