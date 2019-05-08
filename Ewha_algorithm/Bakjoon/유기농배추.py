import sys
sys.setrecursionlimit(100000)
t = int(sys.stdin.readline())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    map1 = [[0]*n for _ in range(m)]
    group = [[0]*n for _ in range(m)]
    for dd in range(k):
        a,b = map(int,sys.stdin.readline().split())
        map1[a][b] = 1
    def dfs(x,y,cnt):
        group[x][y] = cnt
        for jj in range(4):
            nx,ny = x+dx[jj],y+dy[jj]
            if 0<=nx<m and 0<=ny<n:
                if group[nx][ny] == 0 and map1[nx][ny] == 1:
                    dfs(nx,ny,cnt)
    cnt = 0
    for ll in range(m):
        for ss in range(n):
            if group[ll][ss] == 0 and map1[ll][ss] ==1:
                cnt+=1
                dfs(ll,ss,cnt)
    print(cnt)