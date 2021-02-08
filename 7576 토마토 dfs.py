n, m = map(int, input().split())

graph = []
for i in range(n): # 행 길이 만큼
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우는 즉시 종료
    if x <= 1 or x >= n or y <= -1 or y >= m :
        return False
    # x,y가 미방문 노드이면
    if graph[x][y] == 0:
        graph[x][y] == 1 # 방문처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1) # 상하좌우 물들이기
        return True
    return False

# 연결 가능한 요소들 카운트
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1
print(result)