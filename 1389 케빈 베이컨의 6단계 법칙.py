import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
#big_m = 1000000 # 여기에 큰수를 넣는 이유는?
arc = [[n-1 for _ in range(n)] for _ in range(n)] # n*n 관계행렬

for _ in range(m): #m은 연결된 arc 수
   a, b = map(int, input().split())
   arc[a-1][b-1] = 1 # 연결되어있음을 확인해줌
   arc[b-1][a-1] = 1 # 직결되어있으면 1 아니면 big_m
print(arc) # 연결되면 1, 아니면 n-1
for k in range(n): # 연결노드를 위해 k
    arc[k][k] = 0  # 자기자신은 0으로 초기화 # 반복 가장 적게하기 위해 for문내 제일 밖으로
    for i in range(n):
        for j in range(n):
            arc[i][j] = min(arc[i][j], arc[i][k]+arc[k][j]) # 연결 되어있으면 더하기
print('2:',arc)
bacon = []
for i in range(n): # 행만큼 반복
    heapq.heappush(bacon, (sum(arc[i]), i+1))# 최소찾기
#bacon.sort(key=lambda x: (x[1],x[0])) #bacon 수대로 정렬

#첫번째 원소에서 index 프린트
print(bacon)
print(bacon[0][1])
