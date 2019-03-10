for i in range(int(input())):
    number,t = map(int,input().split())
    number = list(str(number))
    pop_number = []
    l,c = 0,0
    result = []
    for pp in range(len(number)):
        number[pp] = int(number[pp])
        pop_number.append(number[pp])
    while l<t:
        s =len(number)-1
        max_num = 0
        while s>=0:
            for qq in pop_number:
                max_num = max(qq, max_num)
            if max_num == number[s]:
                if number[s] == number[c]:
                    if not pop_number:
                        break
                    pop_number.remove(number[s])
                    s = len(number) - 1
                    c += 1
                    break
                else:
                    pop_number.remove(number[s])
                    number[s],number[c] = number[c],number[s]
                    c += 1
                    l += 1
                r = 0
                for ss in range(len(number)):
                    r= r+pow(10,(len(number)-(ss+1)))*number[ss]
                result.append(r)
                break
            s -= 1
    for oo in result:
        if max_num<oo:
            max_num = oo
    print(max_num)



