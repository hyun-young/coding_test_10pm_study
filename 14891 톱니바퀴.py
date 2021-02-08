# 시계(1)방향이라면 index 오른쪽으로 밀림 (끝원소 처음에서 밀어넣기)
# 반시계(-1)방향이면 index 왼쪽으로 밀림(처음원소 끝쪽에서 밀어넣기)
# 맞닿는 부분은 3가지 index
# 톱니 [0][2]-[1][6],[1][2]-[2][6],[2][2]-[3][6]
# 톱니바퀴[1][2]는 양 옆에게 영향을 줌
import sys
from collections import deque
input = sys.stdin.readline

wheel= []
stack = []
q = deque()
initial_way =[0,0,0,0]
for _ in range(4):
    wheel.append(deque(map(int,input().strip())))

# 영향을 주는 것 찾아보기 green zone
for i in range(1,4):
    if wheel[i-1][2] + wheel[i][6] == 1:
        stack.append((i-1, i)) # greenzone
copy_stack = stack.copy()



def rotation(idx, clockwise):
    global stack
    print(stack)
    while stack:
        if (idx-1,idx) not in stack and (idx,idx+1) not in stack:
            if clockwise:  # 시계
                clockwise(idx)
            else:   #반시계
                anticlockwise(idx)
            break #여기까진 good
        elif idx == 3:
        elif (idx-1, idx) in stack:
            stack.remove((idx-1, idx))
            rotation(idx,clockwise)
            way = -way
            idx += 1
        elif (idx, idx+1) in stack:
            stack.remove((idx, idx+1))
        sibal(idx, clockwise)
            way = -way
            idx -= 1
        rotation(idx, way)
    return


def sibal(idx, clockwise):
    if clockwise:
        return wheel[idx].rotate(1)
        # wheel[idx].appendleft(wheel[idx].pop())
        # wheel[idx][-1] + wheel[idx][0:-1]
    else:
        return wheel[idx].rotate(-1)
        # wheel[idx].appendleft(wheel[idx].pop())
        # wheel[idx][1:] + wheel[idx][0]




#회전

R = int(input())
for i in range(R):
    idx, clockwise = map(int, input().split())
    idx -= 1
    initial_way[idx] = clockwise
    if stack:
    print('1번째',wheel[idx])
    rotation(idx, way)
    stack = copy_stack
    print('2번째',wheel[idx])
ans = 0
for i in range(4):
    ans += 2**i * wheel[i][0]
print(ans)


    #else : # 반시계



'''elif idx == 1:
    elif idx == 2:
    elif idx == 3:

        idx_13 = idx
    for j in range(8): # 톱니 수
    if way == 1: #시계방향이라면
        if
        wheel[idx][j]'''