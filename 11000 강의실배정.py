import heapq
import sys

input = sys.stdin.readline
n = int(input())
timetable= []
for _ in range(n):
    timetable.append((list(map(int,input().split()))))
timetable.sort()
heap = []
print(timetable)

for s, t in timetable:
    heapq.heappush(heap, t)  # 종료시간 집어넣기
    #print(heap)
    if heap[0] <= s:
        heapq.heappop(heap)
result = len(heap)
print(result)


