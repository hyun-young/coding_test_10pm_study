# 1 2
# 3 4 순으로 나열하는 것
# 모두 1이면 1, 모두 0이면 0,
# 마지막에 좌표 4개뿐이면 더이상 분할안되므로 그대로 출력

import sys
input = sys.stdin.readline

# 4분할 해주기
def quadtree(a,b,n): #a,b는 좌표
    standard = screen[a][b]
    for i in range(a, a + n):
        for j in range(b, b + n):
            if standard != screen[i][j]:
                #통일이 아니라면 사등분
                # 4등분 시작
                print('(',end='')
                n //= 2
                quadtree(a,b,n) #1
                quadtree(a,b+n,n)#2
                quadtree(a+n,b,n)#3
                quadtree(a+n,b+n,n)#4
                print(')', end='')
                return
    if standard == 0:
        print('0', end='')
        return
    elif standard == 1:
        print('1', end='')
        return

n = int(input()) # 2의 제곱수 1<=n<=64
screen = [(list(map(int,input().strip())))for _ in range(n)] # n by n]
quadtree(0,0,n)




