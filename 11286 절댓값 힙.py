import sys
import heapq

input = sys.stdin.readline

n = int(input()) #1<=n<=100000
integer_list = []

for i in range(n):
    x = int(input())
    if (x == 0) & (len(integer_list) == 0):
        print(0) # 비어있을때
    elif x == 0:
        print(heapq.heappop(integer_list)[1]) #리스트가 비어있을 때는 해당 안되므로, 원소는 반드시 존재한다.
    else:
        heapq.heappush(integer_list, (abs(x), x))

'''
for i in range(n):
    x = int(input())
    if (x == 0) & (len(integer_list)==0):
        print(0) # 비어있을때
    elif x == 0:
        print(heapq.heappop(integer_list)[1]) #리스트가 비어있을 때는 해당 안되므로, 원소는 반드시 존재한다.
        #print(integer_list.pop(0)[1])
        #heapq.heappop(integer_list))
        #print('0넣을때',integer_list)
    else:
        heapq.heappush(integer_list, (abs(x), x))
        #print(i,'번째 리스트',integer_list)
        #print('길이',len(integer_list))
#print(integer_list)
'''
