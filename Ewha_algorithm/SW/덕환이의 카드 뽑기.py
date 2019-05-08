T = int(input())
for i in range(T):
    n,k = map(int, input().split())
    k = k + 1
    a = (k)%2
    x = 3
    while x <= n :
        y = k % x
        a = (y + a) % x
        x += 1
    a = a + 1
    print(f"#{i+1} {a}")