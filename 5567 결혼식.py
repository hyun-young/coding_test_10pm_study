from sys import stdin

input = stdin.readline
big_m = 1e9
n = int(input()) # 상근이 포함 총 동기의 수(index는 학번)
m = int(input()) # 관계의 수
matrix = [[big_m for _ in range(n)] for _ in range(n)]
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1 # 친구관계 바꿔써도 상근 행에 1이 들어가도록

for k in range(n):
    for j in range(n):
        matrix[j][j] = 0
        matrix[0][j] = min(matrix[0][j], matrix[0][k] + matrix[k][j])
for j in range(n):
    if 1 <= matrix[0][j] <= 2:
        cnt += 1
print(cnt)




'''arc = [[n - 1 for _ in range(n)] for _ in range(n)]  # n*n 관계행렬

    for k in range(n):  # 연결노드를 위해 k
        arc[k][k] = 0  # 자기자신은 0으로 초기화 # 반복 가장 적게하기 위해 for문내 제일 밖으로
        for i in range(n):
            for j in range(n):
                arc[i][j] = min(arc[i][j], arc[i][k] + arc[k][j])  # 연결 되어있으면 더하기
    print('2:', arc)
    bacon = []
    for i in range(n):  # 행만큼 반복
        heapq.heappush(bacon, (sum(arc[i]), i + 1))'''  # 최소찾기
        
    # bacon.sort(key=lambda x: (x[1],x[0])) #bacon 수대로 정렬
