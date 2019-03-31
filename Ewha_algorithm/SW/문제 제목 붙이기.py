from string import ascii_uppercase;

alpha_list = list(ascii_uppercase)
a,k = {},0
for i in alpha_list:
    a[i] = k
    k+=1

for k in range(int(input())):
    n = int(input())
    start,b,new = 0,[],[]
    for j in range(n):
        b.append(input())
    for q in range(n):
        new.append(a[b[q][0]])
    new = list(set(new))
    new.sort()
    if new[0] != start:
        result = 0
    else:
        for p in new:
            if p == start:
                start+=1
            else:
                break
        result = start
    print(result)