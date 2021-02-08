import sys
from collections import deque
input = sys.stdin.readline

# R: 배열 순서를 뒤집기
# D: 첫번째 숫자 버리기(비어있으면 ERROR)

# RDD: 배열뒤집고 처음 두숫자를 버리기
# DRD : 첫숫자버리고 뒤집고 또 첫숫자 버리고

T = int(input())
for _ in range(T):
    cnt_r = 0
    cnt_d = 0
    rd = input().rstrip()
    print(rd)
    n = int(input()) # 배열에 들어있는 숫자 개수
    write = deque(input()[1:-1].split(','))
    #rite = input()[1:-1].split(',')
    #write = input().rstrip()
    '''for value in write:
        if (value == '[') or (value == ']') or (value == ','):
            del value
        elif int(value) in number:
            num_q.append(int(value))'''
    for i in range(len(rd)):
        if rd[i] == 'R':
            cnt_r += 1
        elif rd[i] == 'D':
            cnt_d += 1
            if len(write) == 0:
                break
            if cnt_r % 2 == 0: #지금까지 r이 짝수개(리버스 한번으로 간주)
                write.popleft()
            else: # 반전이 된 경우는 뒤에서 제거
                write.pop()


    #if (cnt_d == 0) and (cnt_r % 2 == 1): # d가 하나도 없었다면
     #   write.reverse()
    # 출력 부분
    if n < cnt_d:
        print('error')
    else:
        if cnt_r % 2 == 0:
            print("[", end="")
            print(",".join(write), end="")
            print("]")
        else:
            write.reverse()
            print("[", end="")
            print(",".join(write), end="")
            print("]")
