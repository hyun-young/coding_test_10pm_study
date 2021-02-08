# 1461 도서관 문제

import sys
input = sys.stdin.readline
#최소 걸음 수를 계산

n, m = map(int,input().split())
spot = list(map(int, input().split()))
plus = [] # + 방향
minus = [] # - 방향
spot.sort()
walk_minus = []
walk_plus = []
max_minus = 0   # 초기값 지정안하면, 한 쪽 방향만 입력시 인식 못함
max_plus = 0    # 초기값 지정안하면, 한 쪽 방향만 입력시 인식 못함

for i in range(len(spot)):
    if spot[i] <= 0:
        minus.append(spot[i])
    else:
        plus.append(spot[i])

# 현재 작은 순으로 정렬
#print(minus)
#print(plus)

while 1: # minus 방향의 walk 해야되는 값 구하기 #앞방향
    if len(minus) > 0:
        walk_minus.append(abs(minus.pop(0)))
    for _ in range(m - 1):
        if minus:
            minus.pop(0)
    if len(minus) == 0:
        break

while 1: # plus 방향의 walk 해야하는 값 구하기 # 뒷방향
    if len(plus) > 0:
        walk_plus.append(plus.pop())
    for _ in range(m-1): # m-1개는 walk에 안 넣어줌
        if plus:
            plus.pop()
    if len(plus) == 0:
        break
#print(walk_plus)
#print(walk_minus)
# max값 갱신
# 만약에 비어있으면(한방향이면) 초기값 0으로 생각
if len(walk_minus) != 0:
    max_minus = max(walk_minus)
if len(walk_plus) != 0:
    max_plus = max(walk_plus)

#print(walk_plus)
#print(walk_minus)
ans = (sum(walk_minus) + sum(walk_plus)) * 2 #- max(max_plus, max_minus)
if max_plus >= max_minus:
    ans -= max_plus
else:
    ans -= max_minus
print(ans)




