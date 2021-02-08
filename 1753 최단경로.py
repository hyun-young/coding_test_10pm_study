import heapq

# v  정점 개수, e 간선 개수
v, e = map(int,input().split())
arr = [[] for _ in range(v+1)]
distance = [1e9] * (v+1)
start = int(input()) # 시작 정점번호
distance[start] = 0

for _ in range(e):
    a, b, w = map(int,input().split())
    arr[a].append((w,b))

heap = []

for w, b in arr[start]:
    heapq.heappush(heap,(w,b))

while heap:
    weight, target = heapq.heappop(heap)
    if distance[target] > weight: # 최소의 weight가 되도록 설정한 것
        #print('이부분', distance[target], weight)
        distance[target] = weight
        for w, b in arr[target]:
            print('arr',arr[target])
            print('weight', weight)
            heapq.heappush(heap,(w+weight, b))


# 출력부
for value in distance[1:]: # 총 v개
    if value == 1e9: #경로 존재 x
        print('INF')
    else:
        print(value)

