for i in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    b = []
    for k in a:
      b.append(int(k))
    max = 0
    min = 0
    for s in range(len(b)):
        if s<len(b)-1:
            if b[s]-b[s+1]<0:
                if b[s]-b[s+1]<min:
                    min = b[s]-b[s+1]
            else:
                if b[s]-b[s+1]>max:
                    max = b[s]-b[s+1]
    r = '#'+str(i+1)
    print(r,abs(min),max)

