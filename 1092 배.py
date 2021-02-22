import sys
import heapq

def heapsort(x_list):
    heap = []
    result = []
    for i in x_list:
        heapq.heappush(heap, -i)
    for j in range(len(heap)):
        result.append(-heapq.heappop(heap))
    return result



input = sys.stdin.readline
n = int(input())# 크레인
limit = heapsort(list(map(int,input().split())))
m = int(input())
kg = heapsort(list(map(int,input().split())))
min = 0

if limit[0] < kg[0]: # 크레인 이동 불가
    print(-1)
else:
    # 9 8 4
    # 3 3
    while len(kg):
        min += 1
        for idx in range(len(limit)):
            flag = True
            for i in range(len(kg)):
                if limit[idx] >= kg[i]:
                    kg.pop(i)
                    flag = False
                    break # 다음 크레인으로 넘어가게 해줌
            if flag: # 특정 크레인이 모든 box에 대해 무게를 못 실은 경우
                print(min)
                print('here')
                limit = limit[0:idx] # 내림차순이므로 그 idx 전까지로 slicing
                print(limit)
                break
    print(min)
