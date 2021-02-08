import sys
import heapq
input = sys.stdin.readline

n = int(input())
card =[]
for _ in range(n):
    heapq.heappush(card, int(input()))# 힙으로 정렬해줌
print(card)
if n == 1:
    print(0) # card 개수 1 일때 비교안함
else:
    result = 0 # 더해주는 결과값
    while len(card) > 1: # 리스트가 계속 줄어들테니
        first = heapq.heappop(card) #첫번째 뽑아냄
        second = heapq.heappop(card) #두번째 뽑아냄
        result += first + second
        heapq.heappush(card, first + second) # 리스트에 넣어주고 또 정렬
        print(result)
    print('최종결과:',result)
    #print('힙팝 후: ',card) #힙팝 후엔 사라짐
    #print('첫번째 힙팝은? ', a)
    #print('두번째 힙팝은? ', b)
