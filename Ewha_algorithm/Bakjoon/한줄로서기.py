n = int(input())
a = list(map(int,input().split()))

new_list = []
new_list.append(len(a))

for i in range(len(a)-1,0,-1):
    num = a[i-1]
    k = 0
    while k<num:
        k+=1
    new_list.insert(k,i)

for j in new_list:
    print(j,end=" ")


