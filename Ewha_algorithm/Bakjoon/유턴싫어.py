from collections import deque
r,c = map(int,input().split())
a = [list(map(str,input())) for _ in range(r)]
check = [[0] * c for _ in range(r)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
q = deque()

def bfs(x,y):
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if a[nx][ny] == '.':
                    check[nx][ny]+=1

for k in range(r):
    for j in range(c):
        if a[k][j] == '.':
            bfs(k,j)
result = 0
for k in range(r):
    for j in range(c):
        if check[k][j] == 1:
            result = 1
            break
print(result)

