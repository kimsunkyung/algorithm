for i in range(int(input())):
    s = "#"+str(i+1)
    n,m = map(int,input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))
    result = [0]*len(n_list)
    for k in m_list:
        for j in range(len(n_list)):
            if k>=n_list[j]:
                result[j]+=1
                break
    max = 0
    r = 0
    for q in range(len(result)):
        if result[q]>max:
            max = result[q]
            r = q
    print(s,r+1)
